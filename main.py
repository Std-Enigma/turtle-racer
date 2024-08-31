import random
from turtle import Screen, Turtle

is_game_over = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("light slate gray")

turtles = []
bet = screen.textinput(
    title="Who's the winner", prompt="Which turtle will win the race? Enter a Color?: "
).lower()

for index in range(6):
    timmy = Turtle(shape="turtle")
    timmy.penup()
    timmy.color(colors[index])
    timmy.goto(x=-240, y=-100 + index * 40)
    timmy.pendown()
    turtles.append(timmy)

winner = None

while not is_game_over:
    for turtle in turtles:
        if turtle.xcor() > 230:  # screen_width / 2 - turtle_width
            winner = turtle.pencolor()
            is_game_over = True
            break
        speed = random.randint(1, 15)
        turtle.forward(speed)

if winner == bet:
    print(f"Nice you have guess it correctly.")
else:
    print(f"Sorry you lost the bet.")
print(f"The winner was the {winner} turtle.")

screen.exitonclick()
