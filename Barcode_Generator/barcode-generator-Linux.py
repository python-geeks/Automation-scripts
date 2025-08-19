# -*- coding:UTF-8 -*-

import re, os, sys, upcean, csv;
from configparser import ConfigParser
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mbox
from tkinter import filedialog as fdial
from PIL import Image, ImageTk;
import tkinter.scrolledtext as tkst


class MainWin(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self)
        master.geometry(set_size(master, 520, 450))
        master.resizable(False, True)
        master.title("Barcode generator v1.0")

        self.barcode_bg_color = (255, 255, 255);
        self.barcode_bar_color = (0, 0, 0);
        self.barcode_text_color = (0, 0, 0);
        self.barcode_list = {"EAN-13": "ean13", "EAN-8": "ean8", "EAN-5": "ean5"};
        self.bcsize = tk.IntVar()
        self.bctype = tk.StringVar()
        self.bcvalue = tk.StringVar()
        self.ean13start = self.ean08start = self.ean05start = ''
        self.existcomment = ''
        self.filedir = ''
        self.filetype = 'PNG'
        self.edited = False
        self.selected = ''
        self.oldvalue = ''


        self.master = master
        master.rowconfigure(1, weight=1)
        self.frameTopLeft = tk.Frame(master)
        self.frameTopLeft.grid(row=0, column=0, sticky='nw', padx=(10, 0))
        self.frameTopRight = tk.Frame(master, width=280)
        self.frameTopRight.grid(row=0, column=1, sticky='nsw', padx=(0, 0))
        self.frameTopRight.grid_propagate(False)
        self.frameMain = ttk.Frame(master)
        self.frameMain.grid(row=1, column=0, columnspan=2, sticky='nswe', padx=(10, 0), pady=(0,10))

        # Menubar
        master.option_add('*tearOff', False)
        self.menubar = tk.Menu(master)
        master.config(menu = self.menubar)
        self.file = tk.Menu(self.menubar)
        help_ = tk.Menu(self.menubar)

        self.menubar.add_cascade(menu = self.file, label = 'File')

        self.file.add_command(label = 'Save as', command = self.saveasfile)
        self.file.add_command(label = 'Settings', command =self.settings)
        self.file.add_command(label = 'Info', command =self.helpwin)
        self.file.entryconfig('Save as', accelerator = 'Ctrl+S')

        #Entries
        self.frameType = ttk.Frame(self.frameTopLeft, padding=(5, 5))
        self.frameType.grid(row=0, column=0, sticky="nswe", padx=(0,0), pady=(2,2))
        ttk.Label(self.frameType, text='Barcode type:  ').grid(row=0, column=0, sticky='w', pady=(0,0))
        options = ['EAN-13', 'EAN-8', 'EAN-5']
        self.bcode_type = ttk.OptionMenu(self.frameType, self.bctype, options[0], *options, style = 'raised.TMenubutton')
        self.bcode_type.config(width=10)
        self.bcode_type.grid(row=0, column=1, sticky='we')

        self.frameSize = ttk.LabelFrame(self.frameTopLeft, text="Barcode size:", padding=(3, 3))
        self.frameSize.grid(row=1, column=0, sticky="nswe", padx=(5,5), pady=(2,2))
        self.bcode_size = ttk.Scale(self.frameSize, value=1, from_=1, to=10, variable=self.bcsize, command=self.setscale)
        self.bcode_size.grid(row=0, column=0, sticky='we', pady=(5,0))
        ttk.Label(self.frameSize, text='   1   2   3   4   5   6   7   8   9  10 ').grid(row=1, column=0, sticky='w')

        ttk.Label(self.frameTopLeft, text='Barcode value:').grid(row=2, column=0, sticky='w', padx=(5, 0))
        self.bcode_val = ttk.Entry(self.frameTopLeft, width=17, textvariable=self.bcvalue, font=('Arial', 21))
        self.bcode_val.grid(row=3, column=0, pady=(0,0))

        ttk.Label(self.frameTopLeft, text='Comment:').grid(row=4, column=0, sticky='w', padx=(5, 0), pady=(5,0))
        self.textFrame = ttk.Frame(self.frameTopLeft, height=50, width=180)
        self.textFrame.grid(row=5, column=0, pady=(0,0))
        self.textFrame.columnconfigure(0, weight=1)
        self.bcode_comment = tkst.ScrolledText(self.textFrame, wrap=tk.WORD, width=23, height=3, font=('Arial', 15))
        self.bcode_comment.grid(row=0, column=0, pady=(0,0), sticky='we')

        # Buttons
        self.frameButton = ttk.Frame(self.frameTopRight)
        self.frameButton.grid(row=0, column=0, sticky="nswe", padx=(0,5), pady=(5,5))
        self.frameButton.grid_columnconfigure(0, weight=1)
        self.frameButton.grid_columnconfigure(1, weight=1)
        self.btnGenerate = ttk.Button(self.frameButton, text='Generate', command=self.generate)
        self.btnGenerate.grid(row=0, column=0, pady=(0,0), padx=(0, 2), sticky="we")
        self.btnSave = ttk.Button(self.frameButton, text='Save', command=self.saveasfile)
        self.btnSave.grid(row=0, column=1, pady=(0,0), padx=(2, 0), sticky="we")

        # Preview
        self.imagepanel = tk.Canvas(self.frameTopRight, width=250, height=175);
        self.imagepanel.configure(background='#c1c1c1')
        self.imagepanel.config(highlightbackground='#5f5f5f')
        self.vsb = ttk.Scrollbar(self.frameTopRight, orient="vertical", command=self.imagepanel.yview)
        self.hsb = ttk.Scrollbar(self.frameTopRight, orient="horizontal", command=self.imagepanel.xview)
        self.vsb.grid(row=1, column=1, sticky="nse")
        self.hsb.grid(row=2, column=0, sticky="sew")
        self.imagepanel.config(yscrollcommand=lambda f, l: self.autoscroll(self.vsb, f, l))
        self.imagepanel.config(xscrollcommand=lambda f, l:self.autoscroll(self.hsb, f, l))
        self.imagepanel.grid(row=1, column=0, sticky ="nswe", padx=(0,5), pady=(0,5))


        # Table
        self.frameMain.rowconfigure(0, weight=1)
        self.tree = ttk.Treeview(self.frameMain, selectmode="extended", height=10, columns=("barcodes","type",
            "comment"),
            displaycolumns="barcodes type comment")
        self.tree.grid(row=0, column=0, sticky="ns", padx=(5,5), pady=(5,5))
        self.vsb1 = ttk.Scrollbar(self.frameMain, orient="vertical", command=self.tree.yview)
        self.hsb1 = ttk.Scrollbar(self.frameMain, orient="horizontal", command=self.tree.xview)
        self.vsb1.grid(row=0, column=1, sticky="nse")
        self.hsb1.grid(row=1, column=0, sticky="sew")
        self.tree.config(yscrollcommand=lambda f, l: self.autoscroll(self.vsb1, f, l))
        self.tree.config(xscrollcommand=lambda f, l:self.autoscroll(self.hsb1, f, l))
        self.tree.heading("#0", text="#")
        self.tree.heading("barcodes", text="Barcodes")
        self.tree.heading("type", text="Type")
        self.tree.heading("comment", text="Comment")

        self.tree.column("#0",minwidth=20, width=55, stretch=True, anchor="center")
        self.tree.column("barcodes",minwidth=50, width=120, stretch=True, anchor="center")
        self.tree.column("type",minwidth=40, width=65, stretch=True, anchor="center")
        self.tree.column("comment",minwidth=120, width=240, stretch=True, anchor="center")

        self.tree.tag_configure('even', background='#d9dde2')
        self.tree.bind('<Double-Button-1>', self.edit)
        master.bind("<Escape>", self.exit_ui);
        master.bind('<Control-s>', self.saveasfile)

        self.get_from_ini()
        self.read_file()

    def updatecomment(self, value=None):
        self.bcode_comment.delete(1.0, tk.END)
        if value:
            self.bcode_comment.insert(tk.END, value)

    def clearall(self):
        self.bcode_comment.delete(1.0, tk.END)
        self.bcode_val.delete(0, 'end')

    def edit(self, event):
        w = event.widget
        self.selected = w.focus()
        self.edited = True
        if self.selected:
            values = self.tree.set(self.selected)
            self.oldvalue = values['barcodes']
            self.bcvalue.set(values['barcodes'])
            self.updatecomment(values['comment'])
            self.bctype.set(values['type'])
            self.previewbarcode(values['barcodes'])


    def generate(self):
        if not self.bcvalue.get() or self.edited:
            self.clearall()
            if not self.GenerateCode():
                return False
        self.previewbarcode(self.bcode_val.get())
        self.edited = False


    def saveasfile(self, event=None):
        if self.bcode_val.get():
            if event:
                self.savebarcode(self.bcode_val.get())
            else:
                self.savebarcode(self.bcode_val.get(), True)
            self.updatetree()
        else:
            mbox.showwarning("Warning", "Generate any barcode first!");


    def generatebarcode(self, bcodevalue):
        tmpbarcode = upcean.oopfuncs.barcode(self.barcode_list[self.bctype.get()], self.bcode_val.get());
        tmpbarcode.size = self.bcode_size.get();
        tmpbarcode.barcolor = self.barcode_bar_color;
        tmpbarcode.textcolor = self.barcode_text_color;
        tmpbarcode.bgcolor = self.barcode_bg_color;
        tmpbarcode.filename = None;
        return tmpbarcode


    def previewbarcode(self, bcodevalue):
        tmpbarcode = self.generatebarcode(bcodevalue)
        validbc = tmpbarcode.validate_draw_barcode();
        if(validbc):
            image1 = ImageTk.PhotoImage(validbc);
            self.imagepanel.create_image(validbc.size[0]/2, validbc.size[1]/2, image=image1);
            self.imagepanel.config(scrollregion=(0,0, validbc.size[0], validbc.size[1]));
            self.imagepanel.image = image1;
            self.already_exist(False, bcodevalue)
        else:
            mbox.showerror("Error", "Barcode couldn't be generated!")


    def savebarcode(self, bcodevalue, autoname=False):
        savestate = False;
        fname = "";
        if autoname:
            fname = self.filedir+'/'+ bcodevalue + '.' + self.filetype.lower()
        else:
            fname = fdial.asksaveasfilename(defaultextension='png', parent=self.master, title='Saving barcode', filetypes=[('PNG','*.png'), ('JPEG','*.jpg *.jpeg'), ('GIF','*.gif'), ('Adobe PDF','*.pdf'), ('Barcha fayllar','*.*')]);
        if(fname):
            tmpbarcode = self.generatebarcode(bcodevalue)
            tmpbarcode.filename = fname;
            savestate = tmpbarcode.validate_create_barcode();
            if(not savestate):
                mbox.showerror("Warning", "Barcode saving error");
            else:
                mbox.showinfo("Info", "Barcode is saved as file successfully");


    def updatetree(self):
        bcitem = self.getvalues()
        if self.isunique(bcitem[0]):
            idd = self.last_id()+1
            self.tree.insert('', 'end', idd, text=idd, values = bcitem)
            self.tree.focus_set()
        else:
            if self.edited:
                if self.oldvalue == bcitem[0]:
                    self.tree.set(self.selected, 'comment', bcitem[2])
                    self.tree.selection_set(self.selected)
                else:
                    return self.already_exist()
            else:
                return self.already_exist()
        self.clearall()
        self.edited = False
        self.write_file()
        return True


    def already_exist(self, warn=True, bcode=None):
        if warn:
            mbox.showwarning("Warning", "Barcode is already in table!");
            return False
        else:
            if not self.isunique(bcode):
                self.updatecomment(self.existcomment)


    def last_id(self):
        if self.tree.get_children():
            idmax = max([int(i) for i in self.tree.get_children()])
        else:
            idmax = 0
        return idmax


    def getvalues(self):
        return self.bcvalue.get(), self.bctype.get(), self.bcode_comment.get(1.0, '1.end')


    def GenerateCode(self):
        if self.bctype.get() == 'EAN-13':
            if self.ean13start.isdigit() and len(self.ean13start)>12:
                newcode = int(self.ean13start[:12])
                nextcode = False
                while nextcode == False:
                    if self.validate_ean13(newcode):
                        if self.isunique(str(newcode) +str(self.validate_ean13(newcode))):
                            nextcode == True
                            break
                    newcode += 1
                self.bcvalue.set(str(newcode) +str(self.validate_ean13(newcode)))
                return True
            else:
                mbox.showwarning("Warning", "Enter initial value for EAN-13!");
                return False
        elif self.bctype.get() == 'EAN-8':
            if self.ean08start.isdigit() and len(self.ean08start)>7:
                newcode = int(self.ean08start[:7])
                nextcode = False
                while nextcode == False:
                    if self.validate_ean08(newcode):
                        if self.isunique(str(newcode) +str(self.validate_ean08(newcode))):
                            nextcode == True
                            break
                    newcode += 1
                self.bcvalue.set(str(newcode) +str(self.validate_ean08(newcode)))
                return True
            else:
                mbox.showwarning("Warning", "Enter initial value for EAN-08!");
                return False
        elif self.bctype.get() == 'EAN-5':
            if self.ean05start.isdigit() and len(self.ean05start)==5:
                newcode = int(self.ean05start)
                nextcode = False
                while nextcode == False:
                    if self.isunique(str(newcode)):
                        nextcode == True
                        break
                    newcode += 1
                self.bcvalue.set(str(newcode))
                return True
            else:
                mbox.showwarning("Warning", "Enter initial value for EAN-05!");
                return False


    ############################################################################
    ##                        GIU RELATED OPERATIONS                          ##
    ############################################################################

    def exit_ui(self, event):
        self.master.quit();

    def setscale(self, var):
        value = self.bcode_size.get()
        if int(value) != value:
            self.bcode_size.set(round(value))

    def settings(self):
        setwin = SettingWin(self.master)
        self.get_from_ini()

    def helpwin(self):
        setwin = HelpWin(self.master)

    def autoscroll(self, sbar, first, last):
        """Hide and show scrollbar as needed."""
        first, last = float(first), float(last)
        if first <= 0 and last >= 1:
            sbar.grid_remove()
        else:
            sbar.grid()
        sbar.set(first, last)

    def zebra(self):
        childs = self.tree.get_children()
        if childs:
            n=0
            for child in childs:
                n += 1
                if (n%2==0):
                    tag='even'
                else:
                    tag='odd'
                self.tree.item(child, tags=(tag,))

    ############################################################################
    ##                           FILE OPERATIONS                              ##
    ############################################################################

    # Initializing from config.ini file
    def get_from_ini(self):
        self.config = ConfigParser()
        if not os.path.isfile('config.ini'):
            self.check_inifile()
        self.config.read('config.ini')
        sect = 'DefaultValues'
        try:
            if self.config.get(sect, 'Type'):
                self.bctype.set(self.config.get(sect, 'Type'))
            if self.config.get(sect, 'Size'):
                self.bcsize.set(self.config.get(sect, 'Size'))
            if self.config.get(sect, 'EAN13start'):
                self.ean13start = self.config.get(sect, 'EAN13start')
            if self.config.get(sect, 'EAN08start'):
                self.ean08start = self.config.get(sect, 'EAN08start')
            if self.config.get(sect, 'EAN05start'):
                self.ean05start = self.config.get(sect, 'EAN05start')
            if self.config.get(sect, 'filedirectory'):
                self.filedir = self.config.get(sect, 'filedirectory')
            if self.config.get(sect, 'FileType'):
                self.filetype = self.config.get(sect, 'FileType')
        except:
            mbox.showerror("Warning", "Error occured while loading Config.ini!");


    # Checks and creates if ini file is not found
    def check_inifile(self):
        text = '[DefaultValues]\nType = EAN-13\nEAN13start = 4780000000010\nEAN08start = 47800010\nEAN05start = 00000\nSize = 2\nFileType = PDF\nFileDirectory ='
        file = open('config.ini', 'w')
        file.write(text)
        file.close()


    def write_file(self):
        if self.tree.get_children():
            with open('data.csv', 'w', encoding='utf-8') as file:
                fieldnames = ["id", "barcodes", "type","comment"]
                writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=";")
                writer.writeheader()
                for item in self.tree.get_children():
                    mydata = self.tree.set(item)
                    mydata["id"] = item
                    writer.writerow(mydata)
            self.zebra()

    def read_file(self):
        if os.path.isfile('data.csv'):
            try:
                with open('data.csv', encoding="utf-8") as csvfile:
                    reader = csv.DictReader(csvfile, fieldnames = None, delimiter=";")
                    for row in reader:
                        self.tree.insert("", "end", row["id"], text=row["id"],
                            values=[row["barcodes"], row["type"], row["comment"]])
                self.zebra()
            except:
                mbox.showerror("Error", "Error occured while loading Data.csv!");


    ############################################################################
    ##                          BARCODE VALIDATIONS                           ##
    ############################################################################

    def isunique(self, bcode):
        if os.path.isfile('data.csv'):
            with open('data.csv', encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile, fieldnames = None, delimiter=";")
                for row in reader:
                    if row["barcodes"] == bcode:
                        self.existcomment = row["comment"]
                        return False
                return True
        else:
            return True


    def validate_ean13(self, upc, return_check=False):
        upc = str(upc);
        if(len(upc)>13):
            fix_matches = re.findall("^(\d{13})", upc);
            upc = fix_matches[0];
        if(len(upc)>13 or len(upc)<12):
            return False;
        upc_matches = list(upc);
        upc_matches = [int(x) for x in upc_matches];
        upc_matches1 = upc_matches[0:][::2];
        upc_matches2 = upc_matches[1:][::2];
        EvenSum = (upc_matches2[0] + upc_matches2[1] + upc_matches2[2] + upc_matches2[3] + upc_matches2[4] + upc_matches2[5]) * 3;
        OddSum = upc_matches1[0] + upc_matches1[1] + upc_matches1[2] + upc_matches1[3] + upc_matches1[4] + upc_matches1[5];
        AllSum = OddSum + EvenSum;
        CheckSum = AllSum % 10;
        if(CheckSum>0):
            CheckSum = 10 - CheckSum;
        if(not return_check and len(upc)==13):
            if(CheckSum!=upc_matches1[6]):
                return False;
            if(CheckSum==upc_matches1[6]):
                return True;
        if(return_check):
            return str(CheckSum);
        if(len(upc)==12):
            return str(CheckSum);


    def validate_ean08(self, upc, return_check=False):
        upc = str(upc);
        if(len(upc)>8):
            fix_matches = re.findall("^(\d{8})", upc);
            upc = fix_matches[0];
        if(len(upc)>8 or len(upc)<7):
            return False;
        upc_matches = list(upc);
        upc_matches = [int(x) for x in upc_matches];
        upc_matches1 = upc_matches[0:][::2];
        upc_matches2 = upc_matches[1:][::2];
        EvenSum = (upc_matches1[0] + upc_matches1[1] + upc_matches1[2] + upc_matches1[3]) * 3;
        OddSum = upc_matches2[0] + upc_matches2[1] + upc_matches2[2];
        AllSum = OddSum + EvenSum;
        CheckSum = AllSum % 10;
        if(CheckSum>0):
            CheckSum = 10 - CheckSum;
        if(not return_check and len(upc)==8):
            if(CheckSum!=upc_matches2[3]):
                return False;
            if(CheckSum==upc_matches2[3]):
                return True;
        if(return_check):
            return str(CheckSum);
        if(len(upc)==7):
            return str(CheckSum);





class SettingWin(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self)
        self.top = tk.Toplevel()
        self.top.resizable(False, False)
        self.top.geometry(set_size(self.top, 230, 330))
        self.top.title("Default settings")

        self.default_type = tk.StringVar()
        self.default_size = tk.IntVar()
        self.default_filetype = tk.StringVar()
        self.default_dir = tk.StringVar()
        self.ean13 = tk.StringVar()
        self.ean08 = tk.StringVar()
        self.ean05 = tk.StringVar()

        self.frameMain = ttk.Frame(self.top)
        self.frameMain.grid(row=0, column=0, sticky='nswe', padx=(10,0))
        self.bottom = ttk.Frame(self.top)
        self.bottom.grid(row=1, column=0, sticky='nswe', padx=(10,0))
        self.bottom.columnconfigure(0, weight=1)
        self.bottom.columnconfigure(1, weight=1)


        ttk.Label(self.frameMain, text='Barcode type: ').grid(row=0, column=0, sticky='w', pady=(5,0))
        options = ['EAN-13', 'EAN-8', 'EAN-5']
        self.dbctype = ttk.OptionMenu(self.frameMain, self.default_type, options[0], *options, style = 'raised.TMenubutton')
        self.dbctype.config(width=7)
        self.dbctype.grid(row=0, column=1, pady=(5,0), sticky='we')
        ttk.Label(self.frameMain, text="Barcode size: ").grid(row=1, column=0, sticky='w', pady=(5,0))
        self.dbcsize = tk.Spinbox(self.frameMain, wrap=True, width=5, from_=1, to=10, textvariable=self.default_size);
        self.dbcsize.grid(row=1, column=1, pady=(5,0), sticky='e')
        ttk.Label(self.frameMain, text="Default file type:").grid(row=2, column=0, sticky='w', pady=(5,0))
        filetypes = ['PDF', 'PNG', 'JPG', 'GIF']
        self.dcfiletype = ttk.OptionMenu(self.frameMain, self.default_filetype, filetypes[0], *filetypes)
        self.dcfiletype.config(width=7)
        self.dcfiletype.grid(row=2, column=1, sticky='we', pady=(5,0))
        ttk.Label(self.frameMain, text='EAN-13 initial value:').grid(row=3, column=0, columnspan=2, sticky='w', pady=(5,0))
        self.dean13 = ttk.Entry(self.frameMain, width=26, textvariable=self.ean13)
        self.dean13.grid(row=4, column=0, columnspan=2)
        ttk.Label(self.frameMain, text='EAN-08 initial value:').grid(row=5, column=0, columnspan=2, sticky='w', pady=(5,0))
        self.dean08 = ttk.Entry(self.frameMain, width=26, textvariable=self.ean08)
        self.dean08.grid(row=6, column=0, columnspan=2)
        ttk.Label(self.frameMain, text='EAN-05 initial value:').grid(row=7, column=0, columnspan=2, sticky='w', pady=(5,0))
        self.dean05 = ttk.Entry(self.frameMain, width=26, textvariable=self.ean05)
        self.dean05.grid(row=8, column=0, columnspan=2)

        self.framepdf = ttk.Frame(self.frameMain)
        self.framepdf.grid(row=9, column=0, columnspan=2)
        ttk.Label(self.framepdf, text='File saving directory:').grid(row=0, column=0, sticky='w', pady=(5,0))
        self.dfiledir = ttk.Entry(self.framepdf, width=20, textvariable=self.default_dir)
        self.dfiledir.grid(row=1, column=0, padx=(3, 0), pady=(5,0))
        self.pdfbtn = ttk.Button(self.framepdf, text='...', width=3, command=self.folder)
        self.pdfbtn.grid(row=1, column=1, padx=(5, 0), pady=(5, 0))

        self.skpSave = ttk.Button(self.bottom, text='Save', command=self.save_list)
        self.skpSave.grid(row=0, column=0, sticky='we', padx=(0, 5), pady=(10, 3))
        self.btcancel = ttk.Button(self.bottom, text='Cancel', command=self.cancel)
        self.btcancel.grid(row=0, column=1, sticky='we', padx=(5, 0), pady=(10, 3))

        self.dbcsize.focus_set()

        self.top.bind('<Escape>', self.cancel)

        self.get_from_ini()

        self.top.grab_set()
        master.wait_window(self.top)

    def get_from_ini(self):
        self.partlist=[]
        self.config = ConfigParser()
        self.config.read('config.ini')
        sect = 'DefaultValues'
        self.default_type.set(self.config.get(sect, 'Type'))
        self.default_size.set(self.config.get(sect, 'Size'))
        self.default_filetype.set(self.config.get(sect, 'FileType'))
        self.default_dir.set(self.config.get(sect, 'FileDirectory'))
        self.ean13.set(self.config.get(sect, 'EAN13start'))
        self.ean08.set(self.config.get(sect, 'EAN08start'))
        self.ean05.set(self.config.get(sect, 'EAN05start'))

    def update_list(self):
        self.name.delete(0, 'end')
        self.code.delete(0, 'end')
        self.address.delete(0, 'end')
        self.dockname.delete(0, 'end')
        self.pdfaddress.delete(0, 'end')
        self.name.insert(0, self.compname.get())
        self.code.insert(0, self.compcode.get())
        self.address.insert(0, self.compaddress.get())
        self.dockname.insert(0, self.dock.get())
        self.pdfaddress.insert(0, self.pdfdir.get())

    def folder(self):
        dirpath = fdial.askdirectory(mustexist=False,
                                     parent=self.master, title='Choose the folder')
        if dirpath:
            self.default_dir.set(dirpath)


    def save_list(self):
        sect = 'DefaultValues'
        self.config.set(sect,'Type', self.default_type.get())
        self.config.set(sect, 'Size', self.dbcsize.get())
        self.config.set(sect, 'FileType', self.default_filetype.get())
        self.config.set(sect, 'FileDirectory', self.default_dir.get())
        self.config.set(sect, 'EAN13start', self.ean13.get())
        self.config.set(sect, 'EAN08start', self.ean08.get())
        self.config.set(sect, 'EAN05start', self.ean05.get())
        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)
        self.top.destroy()

    def cancel(self, event=None):
        self.top.destroy()


class HelpWin(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self)
        self.top = tk.Toplevel()
        self.top.resizable(False, False)
        self.top.geometry(set_size(self.top, 220, 150))
        self.top.title("Info")

        ttk.Label(self.top, text='Barcode generator v1.0', font=("Arial", 10, 'bold')).grid(row=0, column=0, padx=(10,10), pady=(15, 0), sticky='nswe')
        ttk.Label(self.top, text='Hamraqulov Boburmirzo © 2017').grid(row=1, column=0, padx=(10,10), pady=(15, 0), sticky='nswe')
        ttk.Label(self.top, text='Telegram: @bzimor').grid(row=2, column=0, padx=(10,10), pady=(5, 0), sticky='nswe')
        ttk.Label(self.top, text='Github: github.com/bzimor').grid(row=3, column=0, padx=(10,10), pady=(5, 0), sticky='nswe')
        ttk.Label(self.top, text='Email: bobzimor@gmail.com').grid(row=4, column=0, padx=(10,10), pady=(5, 0), sticky='nswe')

        self.top.grab_set()
        master.wait_window(self.top)



def set_size(win, w=0, h=0, absolute=True, win_ratio=None):
    winw = win.winfo_screenwidth()
    winh = win.winfo_screenheight()
    if not absolute:
        w = int(winw * win_ratio)
        h = int(winh * win_ratio)
        screen = "{0}x{1}+{2}+{3}".format(w, h, str(int(winw*0.1)), str(int(winh*0.05)))
    else:
        screen = "{0}x{1}+{2}+{3}".format(w, h, str(int((winw-w)/2)), str(int((winh-h)/2)))
    return screen


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path).replace("\\","/")

root = tk.Tk()
app = MainWin(root)
try:
    root.iconbitmap(default=resource_path('app.ico'))
except:
    pass

root.mainloop()
