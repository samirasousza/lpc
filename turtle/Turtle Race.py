import turtle
import random

# Method to get screen
screen = turtle.getscreen()
screen.bgcolor("black")

# Characteristics of the turtle one
player_one = turtle.Turtle()
player_one.color("red")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200, 100)


# Characteristics of the turtle two
player_two = turtle.Turtle()
player_two.color("yellow")
player_two.shape("turtle")
player_two.penup()
player_two.goto(-200, -100)

# Starting position of turtle one
player_one.goto(300, 60)
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(-200, 100)

# Starting position of turtle two
player_two.goto(300, -140)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-200, -100)

# Dice numbers
die = [1, 2, 3, 4, 5, 6]

# The matches of the game
for i in range(20):

    # Player one wins
    if player_one.pos() >= (300, 100):
        print("Player One Wins!")
        break

    # Player two wins
    elif player_two.pos() >= (300, -100):
        print("Player Two Wins!")
        break

    # Dice roll
    else:
        # Turno do jogador um
        player_one_turn = input("Press 'Enter' to roll the die")
        die_outcome = random.choice(die)
        print("The result of the die roll is: ")
        print(die_outcome)
        print("The number of steps will be: ")
        print(20*die_outcome)
        player_one.forward(20*die_outcome)

        # Turno do jogador dois
        player_dois_turn = input("Press 'Enter' to roll the die")
        die_outcome = random.choice(die)
        print("The result of the die roll is: ")
        print(die_outcome)
        print("The number of steps will be: ")
        print(20*die_outcome)
        player_two.forward(20*die_outcome)

turtle.done()
