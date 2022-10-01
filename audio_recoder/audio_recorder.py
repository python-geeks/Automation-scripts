import tkinter as tk
import threading
import pyaudio
import wave


class App():
    chunk = 1024
    sample_format = pyaudio.paInt16
    channels = 2
    fs = 44100

    frames = []

    def __init__(self, master):
        self.isrecording = False
        self.button1 = tk.Button(main, text='Start', width=6,
                                 command=self.startrecording)
        self.button2 = tk.Button(main, text='Stop', width=6,
                                 command=self.stoprecording)
        self.button1.pack()
        self.button2.pack()

    def startrecording(self):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.sample_format,
                                  channels=self.channels, rate=self.fs,
                                  frames_per_buffer=self.chunk, input=True)
        self.isrecording = True
        self.button1['state'] = 'disable'
        print('Recording')
        t = threading.Thread(target=self.record)
        t.start()

    def stoprecording(self):
        self.isrecording = False
        print('Recording Completed')
        self.filename = input('Name the file?')
        self.filename = self.filename + ".wav"
        wf = wave.open(self.filename, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.p.get_sample_size(self.sample_format))
        wf.setframerate(self.fs)
        wf.writeframes(b''.join(self.frames))
        wf.close()
        main.destroy()

    def record(self):
        while self.isrecording:
            data = self.stream.read(self.chunk)
            self.frames.append(data)


main = tk.Tk()
main.title('Audio Recorder')
main.minsize(width=250, height=70)

app = App(main)
main.mainloop()
