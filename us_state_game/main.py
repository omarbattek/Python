import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(750, 600)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

t = turtle.Turtle()
t.hideturtle()
t.penup()

data_state = pandas.read_csv("50_states.csv")
states = data_state["state"]
states_list = states.to_list()



gussed_states = []
# index_states = []

while len(gussed_states) < 50:
    answer_state = screen.textinput(title=f"{len(gussed_states)}/50 State correct", prompt="What's another state name")
    answer_state_title = answer_state.title()

    if answer_state_title == "Exit":
        missing_state = [state for state in states if state not in gussed_states]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("new file.csv")
        break
    if answer_state_title in states_list:
        x = int(data_state[data_state["state"] == answer_state_title]["x"])
        y = int(data_state[data_state["state"] == answer_state_title]["y"])
        t.goto(x, y)
        t.write(answer_state_title)
        gussed_states.append(answer_state_title)
