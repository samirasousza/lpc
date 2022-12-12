import turtle

turtle.speed('fastest')

# Turning the turtle to face upwards
turtle.right(-90)

# The acute angle between
# the base and branch of the y
angle = 30


# Function to draw a colorful Y fractal tree
def get_y_tree(size, level):
    if level > 0:
        turtle.colormode(255)

        # Splitting the rgb range for green
        # into equal intervals for each level
        # setting the colour according
        # to the current level
        turtle.pencolor(0, 255//level, 0)

        # Drawing the base
        turtle.forward(size)
        turtle.right(angle)

        # Recursive call for
        # the right subtree
        get_y_tree(0.8 * size, level-1)
        turtle.pencolor(0, 255//level, 0)
        turtle.left(2 * angle)

        # Recursive call for
        # the left subtree
        get_y_tree(0.8 * size, level-1)
        turtle.pencolor(0, 255//level, 0)
        turtle.right(angle)
        turtle.forward(-size)


# Tree of size 80 and level 7
get_y_tree(80, 7)
