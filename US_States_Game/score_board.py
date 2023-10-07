from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.first_question()

    def first_question(self):
        self.screen.textinput(title="Gues the State", prompt="What's another State's name?").title()

    def update_board(self):
        self.score += 1
        self.screen.textinput(title=f"{self.score}/50 States Correct", prompt="What's another State's name?").title()
