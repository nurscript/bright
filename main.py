from tkinter import Button, Label, Entry, Frame, Tk
from tkinter.font import Font, ITALIC


class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x500")
        self.title("Calculator")
        self.createWidgets()

    def createWidgets(self):
        butts = Button(self,text ="Click")
        butts.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()
