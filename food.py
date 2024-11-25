from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("blue")
        self.refresh()
        self.speed("fastest")

    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-260, 260)
        self.goto(x, y)

