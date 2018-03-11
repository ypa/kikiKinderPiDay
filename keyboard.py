from tkinter import Tk, Label, Button, Text, PhotoImage, END

class NamePad(object):
    def __init__(self, master):
        self.master = master
        master.title("Awesome magical keyboard")

        self.label = Label(master, text="Type in your name and see what it looks like!")
        self.label.pack()

        self.img = PhotoImage(file="./imgs/anna.gif")
        self.text = Text(master)
        self.text.pack(padx=20, pady=20)

        self.greet_button = Button(master, text="Show Image", command=self.show)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def show(self):
        self.text.image_create(END, image=self.img) # Example 1
        self.text.window_create(END, window=Label(self.text, image=self.img))


if __name__ == '__main__':
    root = Tk()
    gui = NamePad(root)
    root.mainloop()
