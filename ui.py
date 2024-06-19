from tkinter import *
THEME_COLOR = "#375362"

class AppUi:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        self.scoretitle = Label(text="Score: 0", font=("Ariel", 20, "italic"), bg=THEME_COLOR, fg="white")
        self.scoretitle.grid(row=0, column=1)

        self.true_img = PhotoImage(file="images/true.png")
        self.false_img = PhotoImage(file="images/false.png")

        self.true_btn = Button(image=self.true_img, highlightthickness=0)
        self.true_btn.grid(row=2, column=0, padx=20, pady=20)

        self.false_btn = Button(image=self.false_img, highlightthickness=0)
        self.false_btn.grid(row=2, column=1, padx=20, pady=20)

        self.window.mainloop()
