import turtle

import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')

# Load new Shape,as we can set/give a particular shape to a turtle---- Remember image type has to be GIF
image = "./US_game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv('./US_game/50_states.csv')
states_list = states_data['state'].to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_states = screen.textinput(title=f"{len(guessed_states)} States Correct",
                                     prompt="What's another State's name?").title()
    if answer_states == "Exit":
        missing_states = [state for state in states_list if state not in guessed_states]

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break
    if answer_states in states_list:
        tur = turtle.Turtle()
        guessed_states.append(answer_states)
        tur.hideturtle()
        tur.penup()
        state = states_data[states_data['state'] == answer_states]
        tur.goto(int(state['x']), int(state['y']))
        tur.write(state['state'].item())



screen.exitonclick()
