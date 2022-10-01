from tkinter import Tk, Button, Toplevel, Label, Frame, PhotoImage, Entry
from tkinter import TOP, LEFT, RIGHT, NE, W, DISABLED, NORMAL, YES
from tkinter import CENTER, BOTH
from tkinter import ttk
import tkinter.messagebox
import os
from mp3Clan_top_web_scraper import findMySong, downloadMySong


class SongGUI:
    def __init__(self, root):
        self.root = root
        self.root.title('Find my tune')
        self.root.geometry()
        self.root.minsize(800, 800)
        self.searchname = tkinter.StringVar()

        # creating help button
        help_button_img = PhotoImage(file='images/help_button.png')
        help_button_img = help_button_img.subsample(2)
        help_img_label = Label(image=help_button_img)
        help_img_label.image = help_button_img
        self.help_button = Button(self.root,
                                  image=help_button_img,
                                  command=self.helpFrame,
                                  border=0)
        self.help_button.pack(side=TOP, anchor=NE, padx=10, pady=10)

        # creating input frame
        self.input_frame = Frame(self.root)
        self.input_frame.pack()

        # creating heading
        heading = Label(self.input_frame, text="Find My Tune",
                        font=("Helvetica", 30), fg="black")
        heading.pack(pady=20, side=TOP)

        # creating search bar
        self.search_box_input = Entry(self.input_frame, font=(
            "Helvetica", 20), textvariable=self.searchname)
        self.search_box_input.pack()

        # creating search button
        search_button_img = PhotoImage(file='images/search_button.png')
        search_button_img = search_button_img.subsample(2)
        search_img_label = Label(image=search_button_img)
        search_img_label.image = search_button_img
        self.search_button = Button(self.input_frame, image=search_button_img,
                                    border=0, command=self.searchSong)
        self.search_button.pack(pady=10, side=LEFT)

        # creating refresh button
        refresh_button_img = PhotoImage(file='images/refresh_button.png')
        refresh_button_img = refresh_button_img.subsample(2)
        refresh_img_label = Label(image=refresh_button_img)
        refresh_img_label.image = refresh_button_img
        self.refresh_button = Button(self.input_frame,
                                     image=refresh_button_img,
                                     fg='green',
                                     command=self.refreshFrame,
                                     border=0)
        self.refresh_button.pack(pady=10, side=RIGHT)

    def helpFrame(self):
        '''shows help Window in new frame'''

        self.help_button['state'] = DISABLED
        # Toplevel object which will be treated as a new window
        self.help_window = Toplevel(self.root)

        # sets the title of the Toplevel widget
        self.help_window.title("Help Window")

        # sets the geometry of toplevel
        self.help_window.geometry("550x800")

        # making help_window unresizable
        self.help_window.resizable(0, 0)

        # reading content from help_window.txt
        info_file = open("help_window.txt")
        lines = info_file. readlines()

        heading = Label(self.help_window, font=(
            "Helvetica 20 underline"), text="HELP WINDOW")
        heading.pack(side=TOP, padx=10, pady=10)

        # code, to show content in help_window
        Label(self.help_window, wraplength=500, justify="left", font=("", 12),
              text=lines[0]).pack(side=TOP, pady=10, padx=5)
        Label(self.help_window, font=("Helvetica 16 underline bold"),
              text="INSTRUCTIONS").pack(anchor=W, padx=10, pady=10)

        for i in range(1, 9):
            Label(self.help_window, wraplength=500,
                  justify="left", font=("", 12),
                  text=str(i) + ". " + lines[i]).pack(anchor=W, pady=2, padx=10)
        Label(self.help_window, font=("Helvetica 16 underline"),
              text="NOTE").pack(anchor=W, padx=10, pady=10)
        for i in range(8, 11):
            Label(self.help_window, wraplength=500,
                  justify="left", font=("", 12),
                  text=str(i - 7) + ". " + lines[i]).pack(anchor=W, pady=2, padx=10)

        self.help_window.protocol("WM_DELETE_WINDOW", self.close_window)

    def close_window(self):
        '''function which closes the help_window'''
        self.help_window.destroy()
        self.help_button['state'] = NORMAL

    def searchSong(self):
        ''''function reads the search_input and searchs for the song'''
        self.songname = self.searchname.get()
        self.searchname.set('')

        # if the search box is not empty
        if (self.songname):

            self.songlist = findMySong(self.songname)
            self.search_button['state'] = DISABLED
            self.searchname.set('')
            self.result_frame = Frame(self.root)
            self.result_frame.pack()
            self.results = ttk.Treeview(self.result_frame)

            # if search is not empty
            if (self.songlist):

                # creates four cols, 1 phantom columns
                self.results['columns'] = ('S.NO', 'Name', 'Duration')

                style = ttk.Style()
                style.configure("Treeview", rowheight=18, columns=30000)

                self.results.column("#0", stretch=YES, width=0, minwidth=0)
                self.results.column("S.NO", stretch=YES, anchor=W, width=40)
                self.results.column("Name", anchor=W, stretch=YES, width=600)
                self.results.column(
                    "Duration", stretch=YES, anchor=W, width=80)

                # Create Headings
                self.results.heading("S.NO", text="S.NO", anchor=W)
                self.results.heading("Name", text="Name", anchor=CENTER)
                self.results.heading("Duration", text="Duration", anchor=W)

                self.results.pack(pady=10, expand=1, fill=BOTH)
                for i in range(len(self.songlist)):
                    self.results.insert(parent='', index='end', iid=i, text='',
                                        values=(str(i + 1),
                                                self.songlist[i]['title'],
                                                self.songlist[i]['duration']))

                self.down_button = Button(
                    self.result_frame, text='DOWNLOAD',
                    fg='white', bg='green',
                    command=self.downloadSong)
                self.down_button.pack(padx=10, side=TOP)

            else:
                tkinter.messagebox.showerror(
                    'No Song Foumd',
                    "Could'nt find your song, please try again")
                self.search_button['state'] = NORMAL

        else:
            tkinter.messagebox.showerror(
                'Search box Empty', "Please enter song name")
            self.search_button['state'] = NORMAL

    def downloadSong(self):
        '''Function which download the song'''

        self.down_button['state'] = DISABLED
        songNumber = self.results.focus()

        # if option is selected
        if (songNumber):
            songNumber = int(songNumber)
            downloadMySong(self.songlist[songNumber]['download-link'])
            filename = [f for f in os.listdir() if f.endswith('.mp3')]
            if (filename):
                # rename file and save in download folder
                os.rename(filename[0], 'downloads/' + filename[0][:-14] + ".mp3")
                tkinter.messagebox.showinfo(
                    'Song Downloaded Successfully',
                    "Your song is downloaded.")
            else:
                tkinter.messagebox.showerror(
                    'Song Not Downloaded',
                    "Could'nt download your song, please try again later.")
                filename = [f for f in os.listdir(
                ) if f.endswith('.crdownload')]
                if (filename):
                    for file in filename:
                        os.remove(file)
        else:
            tkinter.messagebox.showerror(
                'Song Not Selected',
                "Please choose one item from list, then press download button")
        self.down_button['state'] = NORMAL

    def refreshFrame(self):
        '''clears the search window'''
        self.search_button['state'] = NORMAL
        self.searchname.set('')
        try:
            self.result_frame. pack_forget()
        except AttributeError:
            tkinter.messagebox.showinfo(
                'Already Refreshed',
                "window already refreshed")


if (__name__ == "__main__"):
    root = Tk()
    SongGUI(root)
    root.mainloop()
