import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.move, "Up")

cars = []
car_generator_counter = 6


game_is_on = True
while game_is_on:
    time.sleep(0.1/scoreboard.level)
    screen.update()
    
    if car_generator_counter%6 == 0:
        cars.append(CarManager())
    for car in cars:
        #Detect collision with car  
        if player.distance(car) < 25:
            game_is_on = False
            scoreboard.game_over()
            break
        
        car.move()
        
    if player.ycor() > 280:
        player.next_level()
        scoreboard.next_level()
        
    car_generator_counter += 1

screen.exitonclick()