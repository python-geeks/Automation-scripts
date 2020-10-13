import tkinter as tk
import threading
import pyaudio
import wave


class App():
    chunk = 1024
    sample_format = pyaudio.paInt16
    channels = 2
    fs = 44100
    state = ""
    frames = []

    def __init__(self, master):

        self.isrecording = False
        self.button1 = tk.Button(main, text='rec', command=self.startrecording).grid(row=1, column=0)
        self.button2 = tk.Button(main, text='pause', command=self.pause).grid(row=1, column=1)
        self.button3 = tk.Button(main, text='resume', command=self.resume).grid(row=1, column=2)
        self.button4 = tk.Button(main, text='stop', command=self.stoprecording).grid(row=1, column=3)

    def record(self):

        while self.isrecording:
            data = self.stream.read(self.chunk)
            self.frames.append(data)

    def startrecording(self):

        if(self.state == ""):
            self.p = pyaudio.PyAudio()
            self.stream = self.p.open(format=self.sample_format, channels=self.channels,
                                      rate=self.fs, frames_per_buffer=self.chunk, input=True)
            self.isrecording = True
            self.state = "R"
            print('Recording')
            t = threading.Thread(target=self.record)
            t.start()

    def stoprecording(self):

        if(self.state == ""):
            print("Empty Recording Cannot be saved")
        else:
            main.destroy()
            self.isrecording = False
            self.state = "S"
            print('recording complete')
            self.filename = input('\nPlease Enter required Filename\n')
            self.filename = self.filename + ".wav"
            wf = wave.open(self.filename, 'wb')
            wf.setnchannels(self.channels)
            wf.setsampwidth(self.p.get_sample_size(self.sample_format))
            wf.setframerate(self.fs)
            wf.writeframes(b''.join(self.frames))
            wf.close()

    def pause(self):

        if(self.state == "R" or self.state == "Res"):
            self.isrecording = False
            print("Recording Paused")
            self.state = "P"

    def resume(self):

        if(self.state == "P"):
            self.isrecording = True
            self.state = "Res"
            print("Recording Resumed")
            t = threading.Thread(target=self.record)
            t.start()


main = tk.Tk()
main.title('recorder')
main.geometry('200x50')
app = App(main)
main.mainloop()
