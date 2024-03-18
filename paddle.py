from turtle import Turtle
MOVE_DISTANCE = 20
WINDOW_LIMIT = 240
WID = 5
LEN = 1

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=WID, stretch_len=LEN)
        self.penup()
        self.goto(x, y)

    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        if new_y > WINDOW_LIMIT:
            pass
        else:
            self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        if new_y < -WINDOW_LIMIT:
            pass
        else:
            self.goto(self.xcor(), new_y)

