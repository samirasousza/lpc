import turtle

# Screen() method to get screen
screen = turtle.getscreen()

# Creating pen object
pen = turtle.Turtle()


# Function to draw triangles from mouse click events on the screen
def get_triangle(x, y):

    # It is used to draw out the pen
    pen.penup()

    # It is used to move cursor at x
    # and y position
    pen.goto(x, y)

    # It is used to draw in the pen
    pen.pendown()

    # Draw the triangle
    for i in range(3):
        pen.fd(100)
        pen.lt(120)
        pen.fd(100)


# Special built in function to send current
# position of cursor to triangle
turtle.onscreenclick(get_triangle, 1)

turtle.listen()

# Hold the screen
turtle.done()
