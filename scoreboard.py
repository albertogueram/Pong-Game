from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.goto(0, 275)
        self.user = 0
        self.comp = 0
        self.write(f"Computer: {self.comp} | User {self.user}", align="center", font=('Arial', 15, 'normal'))
        self.refresh()


    def refresh(self):
        self.clear()
        self.score += 1
        self.goto(0, 275)
        self.write(f"Computer: {self.comp} | User {self.user}", align="center", font=('Arial', 15, 'normal'))

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        if self.user == 3:
            self.write("CHAMPION!", align="center", font=('Arial', 50, 'normal'))
        if self.comp == 3:
            self.write("GAME OVER!", align="center", font=('Arial', 50, 'normal'))