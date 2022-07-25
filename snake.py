from turtle import Turtle, Screen
import time

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segments(position)

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1500, 1500)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        Screen().update()
        time.sleep(1)

    def add_segments(self, position):
        timmy = Turtle(shape="square")
        timmy.color("white")
        timmy.penup()
        timmy.goto(position)
        self.segments.append(timmy)

    def extend(self):
        self.add_segments(self.segments[-1].position())

    def move_snake(self):
        for seq_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seq_number - 1].xcor()
            new_y = self.segments[seq_number - 1].ycor()
            self.segments[seq_number].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].ycor() + MOVE_DISTANCE != self.segments[1].ycor():
            self.head.setheading(UP)

    def down(self):
        if self.segments[0].ycor() - MOVE_DISTANCE != self.segments[1].ycor():
            self.head.setheading(DOWN)

    def left(self):
        if self.segments[0].xcor() - MOVE_DISTANCE != self.segments[1].xcor():
            self.head.setheading(LEFT)

    def right(self):
        if self.segments[0].xcor() + MOVE_DISTANCE != self.segments[1].xcor():
            self.head.setheading(RIGHT)
