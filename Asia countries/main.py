import turtle
import pandas


screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("Asia countries game")
image = "asia_countries.gif"
screen.addshape(image)

turtle.shape(image)

countries_data = pandas.read_csv("asia_country_code.csv")
all_countries = countries_data.country.to_list()

list_countries = []


while len(list_countries) < 51:
    answer_country = (screen.textinput(title=f"{len(list_countries)}/51 Countries Correct.", prompt="What's the next country")).title()
    if answer_country == "Exit":
        missing_countries = []
        for country in all_countries:
            if country not in list_countries:
                missing_countries.append(country)
                new_data = pandas.DataFrame(missing_countries)
                new_data.to_csv("countries_to_learn.csv")
        break
    if answer_country in all_countries:
        list_countries.append(answer_country)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        country_data = countries_data[countries_data.country == answer_country]
        t.goto(float(country_data.x), float(country_data.y))
        t.write(answer_country, align='center', font=('Arial', 8, 'bold'))


