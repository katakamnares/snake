from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,280)
        self.score_increment()
    def score_increment(self):
        self.write(arg=f"SCORE={self.score}",align="center",font=("arial italic",12,"bold"))

    def update(self):
        self.score+=1
        self.clear()
        self.score_increment()

    def game_over(self):
        self.home()
        self.write(arg="Game Over",align="center",font=("arial italic",12,"bold"))