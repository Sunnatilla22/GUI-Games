import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=1150, height=800)
screen.title("Uzbekistan Regions Games")
image = "regions.gif"
screen.addshape(image)

turtle.shape(image)

regions_data = pandas.read_csv("12_regions.csv")
all_regions = regions_data["regions"].to_list()

list_regions = []

while len(list_regions) < 12:
    answer_region = (
                screen.textinput(title=f"{len(list_regions)}/12 regions Correct", prompt="What's another region's name?")).title()
    if answer_region == "Exit":
        missing_regions = []
        for region in all_regions:
            if region not in all_regions:
                missing_regions.append(region)
                new_data = pandas.DataFrame(missing_regions)
                new_data.to_csv("regions_to_learn.csv")
        break
    if answer_region in all_regions:
        list_regions.append(answer_region)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        region_data = regions_data[regions_data.regions == answer_region]
        t.goto(int(region_data.x), int(region_data.y))
        t.write(answer_region, align='center', font=('Arial', 8, 'bold'))



#
# #finding the location of the states
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# screen.mainloop()