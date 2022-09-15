from turtle import  Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("pink")
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.refresh()

    def refresh(self):
        self.x_coor = random.randint(-250, 250)
        self.y_coor = random.randint(-250, 250)
        self.goto(x=self.x_coor, y=self.y_coor)
