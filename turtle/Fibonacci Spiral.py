import turtle
import math


# Function to draw a fibonacci espiral fractal
def draw_fibonacci(n):
    a = 0
    b = 1
    square_a = a
    square_b = b

    # Setting the colour of the plotting pen to blue
    pen.pencolor("blue")

    # Drawing the first square
    pen.fd(b * factor)
    pen.lt(90)
    pen.fd(b * factor)
    pen.lt(90)
    pen.fd(b * factor)
    pen.lt(90)
    pen.fd(b * factor)

    # Drawing the rest of the squares
    for i in range(1, n):

        # Proceeding in the Fibonacci Series
        temp = square_b
        square_b += square_a
        square_a = temp

        # The rest of the squares
        pen.bk(square_a * factor)
        pen.rt(90)
        pen.fd(square_b * factor)
        pen.lt(90)
        pen.fd(square_b * factor)
        pen.lt(90)
        pen.fd(square_b * factor)

    # Bringing the pen to starting point of the spiral plot
    pen.penup()
    pen.setposition(factor, 0)
    pen.seth(0)
    pen.pendown()

    # Setting the colour of the plotting pen to red
    pen.pencolor("red")

    # Fibonacci Spiral Plot
    pen.left(90)

    for i in range(n):
        print(b)
        fdwd = math.pi * b * factor / 2
        fdwd /= 90

        for j in range(90):
            pen.forward(fdwd)
            pen.left(1)

        temp = a
        a = b
        b = temp + b


# Here 'factor' signifies the multiplicative
# factor which expands or shrinks the scale
# of the plot by a certain factor.
factor = 1

# Taking Input for the number of
# iterations our Algorithm will run
n = int(input("Enter the number of interations (must be > 1): "))

# Plotting the Fibonacci Spiral Fractal
# and printing the corresponding Fibonacci Number
if n > 0:
    print(f"Fibonacci series for {n} elements : ")
    # Screen() method to get screen
    screen = turtle.getscreen()

    # Creating pen object
    pen = turtle.Turtle()

    # Pen speed
    pen.speed(100)

    # Create the Fibonacci Spiral Fractal
    draw_fibonacci(n)

    # Hold the screen
    turtle.done()
else:
    print("Number of iterations must be > 0")
