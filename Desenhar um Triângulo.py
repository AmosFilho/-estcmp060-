import turtle

my_screen = turtle.Screen()
tess = turtle.Turtle()


def triangle(x, y):
    tess.penup()
    tess.goto(x, y)  # It is used to move cursor at x and y position
    tess.pendown()

    for i in range(3):
        tess.forward(100)
        tess.left(120)
        tess.forward(100)


# Special built in function to send current position of cursor to
# triangle
turtle.onscreenclick(triangle, 1)

turtle.listen()
turtle.done()
