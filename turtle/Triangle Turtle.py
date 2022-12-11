import turtle

# Metodo para obter a tela
screen = turtle.getscreen()

# Cria a caneta
pen = turtle.Turtle()


def triangle(x, y):

    # Usado para desenhar sem caneta
    pen.penup()

    # Muda o cursor ate a posicao x e y
    pen.goto(x, y)

    # Usado para desenhar com caneta
    pen.pendown()

    # Desenha o formato do trangulo
    for i in range(3):
        pen.fd(100)
        pen.lt(120)
        pen.fd(100)

# Envia o cursor da posicao atual para o triangulo
turtle.onscreenclick(triangle, 1)

turtle.listen()

# Segura a tela
turtle.done()