import random
import time
from turtle import Screen, Turtle

COLORS = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2

# """Car Manager"""
class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 3:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-235, 240)
            new_car.goto(400, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT


# """"PLAYER""""
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.player_reset()
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def player_reset(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

#  >>>SCOREBOARD<<<

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.color('black')
        self.penup()
        self.goto(x_cor, y_cor)
        self.score = 0
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level : {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)



screen = Screen()
screen.bgcolor('white')
screen.setup(width=800, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard(-300, 260)

for i in range(6):
    car = CarManager()

screen.listen()

screen.onkey(player.move, 'Up')

game_is_on = True


while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    for cars in car_manager.all_cars:
        if player.distance(cars) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.is_at_finish_line():
        player.player_reset()
        scoreboard.increase_score()
        car_manager.speed_up()
screen.exitonclick()