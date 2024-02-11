from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(1,2)
        self.x = 312
        self.y = random.randint(-250, 250)
        self.goto(self.x, self.y)
        self.round = 1
    
    def move(self):
        self.x -= STARTING_MOVE_DISTANCE + (self.round-1)*MOVE_INCREMENT
        self.goto(self.x, self.y)
