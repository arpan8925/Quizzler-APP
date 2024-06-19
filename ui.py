from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class AppUi:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.scoretitle = Label(text="Score: 0", font=("Ariel", 20, "italic"), bg=THEME_COLOR, fg="white")
        self.scoretitle.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(150, 125, width=280, text="Some Question Text", font=("Ariel", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        self.true_img = PhotoImage(file="images/true.png")
        self.false_img = PhotoImage(file="images/false.png")

        self.true_btn = Button(image=self.true_img, highlightthickness=0)
        self.true_btn.grid(row=2, column=0, padx=20, pady=20)

        self.false_btn = Button(image=self.false_img, highlightthickness=0)
        self.false_btn.grid(row=2, column=1, padx=20, pady=20)

        self.next_ques()

        self.window.mainloop()

    def next_ques(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question, text=q_text)
