from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
SCORE_FONT = ("Courier", 15, "normal")
TEXT_FONT = ("Ariel", 15, "italic")


class QuizUI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score : 0", bg=THEME_COLOR, fg="white", font=SCORE_FONT)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=40)

        self.text = self.canvas.create_text(150, 125, width=280, font=TEXT_FONT)

        true_img = PhotoImage(file="images/true.png")
        self.true = Button(image=true_img, highlightthickness=0, command=self.answer_is_true)
        self.true.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.false = Button(image=false_img, highlightthickness=0, command=self.answer_is_false)
        self.false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score : {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text=f"You've completed the quiz.\n"
                                                   f"Your final score : {self.quiz.score}/{self.quiz.question_number}")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def answer_is_true(self):
        is_right = self.quiz.check_answer("true")
        self.feedback(is_right)

    def answer_is_false(self):
        is_right = self.quiz.check_answer("false")
        self.feedback(is_right)

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
