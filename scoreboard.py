from  turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-280, 260)
        self.write(f"Level: {self.level}", align="left", font=FONT)
        
        
    def game_over(self):
        self.goto(0,0)
        self.write("Game over", align="center", font=FONT)
        
    def next_level(self):
        self.level += self.level
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)
