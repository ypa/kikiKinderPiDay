import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

WIDTH = 900
HEIGHT = 1000

class Namepad:

    def __init__(self, root, **kwargs):
        #initialization

        self.__root = root
        self.__thisWidth = kwargs.get('width', WIDTH)
        self.__thisHeight = kwargs.get('height', HEIGHT)
        self.__thisTextArea = Text(self.__root)
        self.__thisMenuBar = Menu(self.__root)
        self.__thisFileMenu = Menu(self.__thisMenuBar,tearoff=0)
        self.__thisEditMenu = Menu(self.__thisMenuBar,tearoff=0)
        self.__thisHelpMenu = Menu(self.__thisMenuBar,tearoff=0)
        self.__thisScrollBar = Scrollbar(self.__thisTextArea)
        self.__file = None

        #set icon
        try:
            self.__root.wm_iconbitmap("Namepad.ico") #GOT TO FIX THIS ERROR (ICON)
        except:
            pass


        #set the window text
        self.__root.title("Untitled - Notepad")

        #center the window
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()

        left = (screenWidth / 2) - (self.__thisWidth / 2)
        top = (screenHeight / 2) - (self.__thisHeight /2)

        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, self.__thisHeight, left, top))

        #to make the textarea auto resizable
        self.__root.grid_rowconfigure(0,weight=1)
        self.__root.grid_columnconfigure(0,weight=1)

        #add controls (widget)

        self.__thisTextArea.grid(sticky=N+E+S+W)

        self.__thisFileMenu.add_command(label="New",command=self.__newFile)
        self.__thisFileMenu.add_command(label="Open",command=self.__openFile)
        self.__thisFileMenu.add_command(label="Save",command=self.__saveFile)
        self.__thisFileMenu.add_separator()
        self.__thisFileMenu.add_command(label="Exit",command=self.__quitApplication)
        self.__thisMenuBar.add_cascade(label="File",menu=self.__thisFileMenu)

        self.__thisEditMenu.add_command(label="Cut",command=self.__cut)
        self.__thisEditMenu.add_command(label="Copy",command=self.__copy)
        self.__thisEditMenu.add_command(label="Paste",command=self.__paste)
        self.__thisMenuBar.add_cascade(label="Edit",menu=self.__thisEditMenu)

        self.__thisHelpMenu.add_command(label="About Notepad",command=self.__showAbout)
        self.__thisMenuBar.add_cascade(label="Help",menu=self.__thisHelpMenu)

        self.__root.config(menu=self.__thisMenuBar)

        self.__thisScrollBar.pack(side=RIGHT,fill=Y)
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)
    
        
    def __quitApplication(self):
        self.__root.destroy()
        #exit()

    def __showAbout(self):
        showinfo("Notepad","Created by: Ferdinand Silva (http://ferdinandsilva.com)")

    def __openFile(self):
        
        self.__file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

        if self.__file == "":
            #no file to open
            self.__file = None
        else:
            #try to open the file
            #set the window title
            self.__root.title(os.path.basename(self.__file) + " - Notepad")
            self.__thisTextArea.delete(1.0,END)

            file = open(self.__file,"r")

            self.__thisTextArea.insert(1.0,file.read())

            file.close()

        
    def __newFile(self):
        self.__root.title("Untitled - Notepad")
        self.__file = None
        self.__thisTextArea.delete(1.0,END)

    def __saveFile(self):

        if self.__file == None:
            #save as new file
            self.__file = asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

            if self.__file == "":
                self.__file = None
            else:
                #try to save the file
                file = open(self.__file,"w")
                file.write(self.__thisTextArea.get(1.0,END))
                file.close()
                #change the window title
                self.__root.title(os.path.basename(self.__file) + " - Notepad")
        else:
            file = open(self.__file,"w")
            file.write(self.__thisTextArea.get(1.0,END))
            file.close()

    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")

    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")

    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")

    def run(self):
        #run main application
        self.__root.mainloop()


if __name__ == '__main__':
    #run main application
    root = Tk()
    namepad = Namepad(root)
    namepad.run()
