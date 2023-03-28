import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

state_data = pandas.read_csv("50_states.csv")

list_state = state_data["state"].to_list()
list_x = state_data["x"].to_list()
list_y = state_data["y"].to_list()

# print(state_data)
sum_of_state = []


# for num in range(1, 51):
def map_game():
    game_is_on = True
    while game_is_on:

        answer_state = (
            screen.textinput(title=f"{len(sum_of_state)}/50 States Correct", prompt="What's another state's name?")).title()

        for state in state_data.state:
            if state == answer_state:
                state_index = list_state.index(state)
                x_cor = list_x[state_index]
                y_cor = list_y[state_index]
                print("it is in")
                new_turtle = turtle.Turtle()
                new_turtle.penup()
                new_turtle.hideturtle()
                new_turtle.goto(x_cor, y_cor)
                new_turtle.write(f"{state}", align='center', font=('Arial', 8, 'normal'))
                sum_of_state.append(new_turtle)
                map_game()
            else:
                game_is_on = False


map_game()

screen.exitonclick()
# a_sate = state_data["state"] == "Alaska"
# print(a_sate.index)
# print(state_data.x[1])

# if answer_state in dict:
#     print("It is in")
# turtle.write(f"{answer_state}",align='left', font=('Arial', 8, 'normal'))

# Finding x and y location of the states
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# screen.mainloop()
