from tkinter import *
THEME_COLOR = "#375362"

class AppUi:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=50, pady=50, background=THEME_COLOR)
        self.canvas = Canvas()
        self.canvas.config(width=300, height=550)
        self.canvas.grid(row=0, column=0)






        self.window.mainloop()