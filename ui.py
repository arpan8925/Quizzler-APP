from tkinter import *
from quiz_brain import QuizBrain
from PIL import Image, ImageTk, ImageSequence

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

        self.true_btn = Button(image=self.true_img, highlightthickness=0, command=self.true_ans)
        self.true_btn.grid(row=2, column=0, padx=20, pady=20)

        self.false_btn = Button(image=self.false_img, highlightthickness=0, command=self.false_ans)
        self.false_btn.grid(row=2, column=1, padx=20, pady=20)

        self.next_ques()

        self.window.mainloop()

    def next_ques(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
            self.scoretitle.config(text=f"Score: {self.quiz.score}")
        else:
            self.quiz_complete()
        
    def true_ans(self):
        self.give_fedback(self.quiz.check_answer("True"))
                
    def false_ans(self):
        is_right = self.quiz.check_answer("False")
        self.give_fedback(is_right)
          

    def give_fedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            print("right")
        else:
            self.canvas.config(bg="red")
            print("Wrong")
        self.window.after(1000, self.next_ques)

    def quiz_complete(self):
        # Hide the buttons
        self.true_btn.grid_remove()
        self.false_btn.grid_remove()
        
        # Animate canvas enlargement
        self.enlarge_canvas(250)

    def enlarge_canvas(self, current_height):
        if current_height < 350:
            new_height = current_height + 10
            self.canvas.config(height=new_height)
            self.window.after(50, self.enlarge_canvas, new_height)
        else:
            self.canvas.itemconfig(self.question, text=f"Hurray! Quiz Complete\nYour Total Score is: {self.quiz.score}/{self.quiz.question_number}")