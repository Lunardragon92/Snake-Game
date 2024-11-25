
from turtle import Turtle,Screen

screen = Screen()
POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segment = []
        self.create()
        self.head = self.segment[0]
    def create(self):
        for position in POSITIONS:
            self.add_segments(position)
    def reset(self):
        for seg in self.segment:
            seg.reset()
        self.segment.clear()
        self.create()
        self.head = self.segment[0]

    def add_segments(self,position):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        tim.setheading(0)
        self.segment.append(tim)
        tim.speed("fastest")

    def extend(self):
        self.add_segments(self.segment[-1].pos())
    def move(self):

        for i in range(len(self.segment) - 1, 0, -1):
            x = self.segment[i - 1].xcor()
            y = self.segment[i - 1].ycor()
            self.segment[i].goto(x, y)

        self.segment[0].forward(MOVE)
    def up(self):
        if self.head.heading()!= DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


