from turtle import Turtle

import pandas

states_data = pandas.read_csv('./US_game/50_states.csv')
states_list = states_data['state'].to_list
ALIGNMENT = 'center'
FONT = ('Arial', 10, 'normal')


class StateGoTo(Turtle):
    def __init__(self, state_name):
        self.state_name = state_name
        super().__init__()
        state = states_data[states_data['state'] == state_name]

        self.hideturtle()
        self.penup()
        self.goto(int(state['x']), int(state['y']))

        self.write(f"{state['state'].item()}", align=ALIGNMENT, font=FONT)
