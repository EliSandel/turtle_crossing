from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.y = -280
    
    def move(self):
        self.y += MOVE_DISTANCE
        self.goto(0,self.y)
    
    def next_level(self):
        self.y = -280
        self.goto(0, self.y)
    
    
        
