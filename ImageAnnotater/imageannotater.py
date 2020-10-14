from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.graphics import Color, Ellipse, Line


import os.path
import numpy as np
import cv2

import glob
im_list = glob.glob("images/*.png")

img_dim = cv2.imread(im_list[0]).shape

img = 0

annotations = []
mode = 0 #0 = draw, 1 = erase

all_annotations = {}

try:
	a = np.load("annotations/annotations.npy")
	all_annotations = a[()]
except Exception, e:
	print e


from kivy.config import Config
Config.set('graphics', 'width', int(img_dim[1]*1.25))
Config.set('graphics', 'height', int(img_dim[0]))
Config.set('graphics', 'resizable', 0)

Builder.load_string('''
<PaintWidget>
	id: 'PaintWidget'
	size_hint_x: 0.8
	size_y:1
	Image:
		source: root.parent.parent.img_src
		opacity: 1.0
<RootWidget>
	BoxLayout:
		orientation: 'horizontal'
		PaintWidget:
		StackLayout:
			size_hint: 0.2, 1
			orientation: 'lr-tb'
			Button:
				text: 'Clear'
				size_hint: 1, None
				on_press: root.clear()
			Button:
				text: 'Next'
				size_hint: 1, None
				on_press: root.change(+1)
			Button:
				text: 'Previous'
				size_hint: 1, None
				on_press: root.change(-1)
			Button:
				text: 'Undo'
				size_hint: 1, None
				on_press: root.changeMode()
''')



class PaintWidget(BoxLayout):


	def on_touch_down(self, touch):
		if self.collide_point(*touch.pos):
			if mode == 1:
				return

			color = (0, 1, 0)
			with self.canvas:
				Color(*color, mode='rgb')
				d = 15
				touch.ud['line'] = Line(points=(touch.x, touch.y), close=True, joint='round')
				global annotations
				#annotations = np.array([touch.x, touch.y])

	def on_touch_move(self, touch):


		if self.collide_point(*touch.pos):

			if mode == 0:#check if draw or delete, will make this work later

				if not touch.ud:
					color = (0, 1, 0)
					with self.canvas:
						Color(*color, mode='rgb')
						d = 15
						touch.ud['line'] = Line(points=(touch.x, touch.y),close = True, joint='round')

				else:
					touch.ud['line'].points += [touch.x, touch.y]
			else:
				for x in annotations:
					if [touch.x, touch.y] in x.tolist():
						del x
						continue

				for x in self.canvas.children:
					if type(x) is Line:
						xs = np.reshape(x.points, (-1, 2))
						del x



	def on_touch_up(self, touch):
		try:
			if len(touch.ud)>0:
				global annotations

				anns = np.reshape(np.asarray(touch.ud['line'].points), (-1, 2))
				annotations.append(anns)

		except Exception, e:
			None





class RootWidget(FloatLayout):

	def __init__(self):
		super(RootWidget, self).__init__()
		self.add_annotations()


	img_src = StringProperty(im_list[img])

	def clear(self):
		self.children[0].children[1].canvas.children = self.children[0].children[1].canvas.children[:1]

		global annotations
		annotations = []

	def add_annotations(self):
		if im_list[img].split("/")[-1] in all_annotations:
			global annotations
			annotations = all_annotations[im_list[img].split("/")[-1]]
			for an in annotations:
				color = (0, 1, 0)
				with self.children[0].children[1].canvas:

					Color(*color, mode='rgb')
					d = 15

					Line(points=np.reshape(an, (1, -1)).tolist()[0],close = True, joint='round')

	def change(self, c):
		global annotations
		image = np.zeros((img_dim[0], img_dim[1]))
		cv2.fillPoly(image, [a.astype(int) for a in annotations ], 255)
		im_name = im_list[img].split("/")[-1]
		name = im_list[img].replace("images", "annotations")
		if not os.path.exists("annotations"):
			os.makedirs("annotations")
		cv2.imwrite(name, np.flipud(image))

		all_annotations[name.split("/")[-1]] = annotations

		np.save("annotations/annotations.npy", all_annotations)


		self.clear()
		global img
		img = (img + c)%len(im_list)
		self.img_src = im_list[img]

		self.add_annotations()

	def changeMode(self):
		if len(self.children[0].children[1].canvas.children) > 3:
			self.children[0].children[1].canvas.children = self.children[0].children[1].canvas.children[:-3]
		global annotations
		annotations = annotations[:-1]

class AnnotatorApp(App):

	def build(self):
		return RootWidget()



if __name__ == '__main__':
	AnnotatorApp().run()
