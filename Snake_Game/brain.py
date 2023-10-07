from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.all_turtles = []
        self.crate_snake()
        self.head = self.all_turtles[0]

    def crate_snake(self):
        for turtle_position in STARTING_POSITIONS:
            self.add_turtle(turtle_position)

    def add_turtle(self, position):
        new_turtle = Turtle(shape='square')
        new_turtle.penup()
        new_turtle.color('white')
        new_turtle.goto(position)
        self.all_turtles.append(new_turtle)

    def extend(self):
        self.add_turtle(self.all_turtles[-1].position())

    def move(self):
        for turtle_num in range(len(self.all_turtles) - 1, 0, -1):
            new_x = self.all_turtles[turtle_num - 1].xcor()
            new_y = self.all_turtles[turtle_num - 1].ycor()
            self.all_turtles[turtle_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)


    def reset_game(self):
        for i in self.all_turtles:
            i.goto(1500, 1500)
        self.all_turtles.clear()
        self.crate_snake()
        self.head = self.all_turtles[0]

    def up(self):
        if self.head.heading() != DOWN:
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
