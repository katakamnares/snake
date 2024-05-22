from turtle import Turtle
class Snake:
    def __init__(self):
        self.x_position=[(0,0),(-20,0),(-40,0)]
        self.segements=[]
        self.create_snake()
    def create_snake(self):
        for position in self.x_position:
            self.update(position)
    def update(self,position):
        tom=Turtle("square")
        tom.color("white")
        tom.penup()
        tom.goto(position)
        self.segements.append(tom)
    def extend(self):
        self.update(self.segements[-1].position())
    def move(self):
        for segement in range(len(self.segements)-1,0,-1):
            new_x=self.segements[segement-1].xcor()
            new_y=self.segements[segement-1].ycor()
            self.segements[segement].goto(new_x,new_y)
        self.segements[0].forward(20)
    def up(self):
        if self.segements[0].heading()!=270:
            self.segements[0].setheading(90)
    def Down(self):
        if self.segements[0].heading()!=90:
            self.segements[0].setheading(270)
    def Right(self):
        if self.segements[0].heading()!=180:
            self.segements[0].setheading(0)
    def Left(self):
        if self.segements[0].heading()!=0:
            self.segements[0].setheading(180)
