#!/usr/bin/env python

import requests
import lxml.html
from AppKit import *
from bs4 import BeautifulSoup

from AppKit import NSClickGestureRecognizer



class StatusItem(NSObject):
    def applicationDidFinishLaunching_(self, notification):
        # create a status bar item
        statusbar = NSStatusBar.systemStatusBar()
        self.statusitem = statusbar.statusItemWithLength_(NSVariableStatusItemLength)

        # create a custom view
        # create a custom view with a larger rectangle
        self.view = NSView.alloc().initWithFrame_(NSMakeRect(0, 0, 200, 20))

        self.view.setWantsLayer_(True)
        self.view.layer().setBackgroundColor_(NSColor.blackColor().CGColor())



        # add the custom view to the status bar item
        self.statusitem.setView_(self.view)

        # update the score
        self.update_score()

        # schedule score update every 30 seconds
        self.timer = NSTimer.scheduledTimerWithTimeInterval_target_selector_userInfo_repeats_(30.0, self, 'update_score', None, True)

        # add the custom view to the status bar item
        # add the custom view to the status bar item
        self.statusitem.setView_(self.view)

        # add a click gesture recognizer to the custom view
        click_recognizer = NSClickGestureRecognizer.alloc().initWithTarget_action_(self, 'enlarge_text')
        self.view.addGestureRecognizer_(click_recognizer)



    def update_score(self):
        # retrieve the live score from the cricbuzz website
        response = requests.get('https://m.cricbuzz.com/')
        soup = BeautifulSoup(response.content, 'html.parser')
        match_element = soup.find(class_="cbz-ui-home-scores cbz-common-match")
        score_text = match_element.text
        print(match_element.text)

        # create an attributed string with the score text and the desired attributes
        font_size = 14.0
        font = NSFont.menuFontOfSize_(font_size)
        attributes = {
            NSFontAttributeName: font,
            NSForegroundColorAttributeName: NSColor.whiteColor()
        }
        score_attributed_text = NSAttributedString.alloc().initWithString_attributes_(score_text, attributes)

        # calculate the size of the attributed string
        size = score_attributed_text.size()

        # scale the font size to fit the available space in the custom view
        max_width = self.view.frame().size.width
        while size.width > max_width:
            font_size = font_size - 1.0
            if font_size <= 0:
                break
            font = NSFont.menuFontOfSize_(font_size)
            attributes[NSFontAttributeName] = font
            score_attributed_text = NSAttributedString.alloc().initWithString_attributes_(score_text, attributes)
            size = score_attributed_text.size()

        # update the score in the custom view
        score_label = NSTextField.alloc().initWithFrame_(NSMakeRect(0, 0, size.width, size.height))
        score_label.setAttributedStringValue_(score_attributed_text)
        score_label.setBezeled_(False)
        score_label.setEditable_(False)
        score_label.setDrawsBackground_(False)
        score_label.setAlignment_(NSTextAlignmentCenter)
        score_label.setTextColor_(NSColor.whiteColor())
        self.view.setSubviews_([score_label])


    def enlarge_text(self):
        # retrieve the score label from the custom view
        score_label = self.view.subviews()[0]

        # increase the font size of the label by 2 points
        font = score_label.font()
        font_size = font.pointSize() + 2.0
        font = NSFont.systemFontOfSize_(font_size)
        score_label.setFont_(font)


    def mouseDown_(self, event):
    # enlarge the text in the custom view
        self.enlarge_text()

def main():
    app = NSApplication.sharedApplication()
    delegate = StatusItem.alloc().init()
    app.setDelegate_(delegate)
    NSApp.activateIgnoringOtherApps_(True)
    app.run()






if __name__ == '__main__':
    app = NSApplication.sharedApplication()
    delegate = StatusItem.alloc().init()
    app.setDelegate_(delegate)
    NSApp.activateIgnoringOtherApps_(True)
    app.run()
