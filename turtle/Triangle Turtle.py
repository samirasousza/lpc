import turtle

t = turtle.Turtle()
s = turtle.getscreen()

def triangle():
    t.fd(100)
    t.lt(120)
    t.fd(100)

turtle.onscreenclick(triangle, 1)

turtle.listen()
turtle.done()
