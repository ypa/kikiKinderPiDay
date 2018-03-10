from tkinter import Tk, Label, Button

class NamePad(object):
    def __init__(self, master):
        self.master = master
        master.title("Awesome magical keyboard")

        self.label = Label(master, text="Type in your name and see what it looks like!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")


if __name__ == '__main__':
    root = Tk()
    gui = NamePad(root)
    root.mainloop()
