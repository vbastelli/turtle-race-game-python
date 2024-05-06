import random
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Player 1, make your bet", prompt="Which turtle is going to win the race? enter a color")
bet2 = screen.textinput(title="Player 2, make your bet", prompt="Which turtle is going to win the race? enter a color")
tims = {
    'color': ["red", "orange", "green", "yellow", "blue", "purple"],
    'turtles': [],
}
fdp = Turtle()

fdp.penup()
fdp.goto(219, 300)
fdp.right(90)
fdp.pendown()
fdp.forward(500)


height = -140


for color in tims['color']:
    tim = Turtle(shape="turtle")
    tim.color(color)
    tim.penup()
    height += 40
    tim.goto(x=-230, y=height)
    tims['turtles'].append(tim)


if bet:
    race_on = True
else:
    print('No bets placed.')


def has_reached(turtle_obj, target_x):
    current_x, current_y = turtle_obj.position()
    return current_x >= target_x


def get_turtle_index(turtle_list, turtle_to_find):
    for index, turtle in enumerate(turtle_list):
        if turtle == turtle_to_find:
            return index


while race_on:
    for turtle in tims['turtles']:
        distance_rand = random.randint(0, 10)
        turtle.forward(distance_rand)
        if has_reached(turtle, 200):
            race_on = False
            winner = (tims['color'][get_turtle_index(tims['turtles'], turtle)])

print(f'The winner is: {winner}')
print(f'"Player 1" bet was: {bet}')
print(f'"Player 2" bet was: {bet2}')

if bet == winner:
    print('Player 1 Wins!')
elif bet2 == winner:
    print('Player 2 Wins!')
else:
    print('You both lose!')


screen.exitonclick()
