# Python program for Plotting Fibonacci
# Spiral fractal using Turtle
import turtle
import math


def plotting_fibonacci(n):
    a = 0
    b = 1
    square_a = a
    square_b = b

    x.pencolor("blue")

    # Drawing the first square
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)

    temp = square_b
    square_b = square_b + square_a
    square_a = temp

    for i in range(1, n):
        # Drawing the rest of the squares
        x.backward(square_a * factor)
        x.right(90)
        x.forward(square_b * factor)
        x.left(90)
        x.forward(square_b * factor)
        x.left(90)
        x.forward(square_b * factor)

        temp = square_b
        square_b = square_b + square_a
        square_a = temp

    # Bringing the pen to starting point of the spiral plot
    x.penup()
    x.setposition(factor, 0)
    x.seth(0)
    x.pendown()

    x.pencolor("red")

    # Fibonacci Spiral Plot
    x.left(90)
    for i in range(n):
        print(b)
        fdwd = (math.pi*b*factor) / 2
        fdwd /= 90
        for j in range(90):
            x.forward(fdwd)
            x.left(1)
        temp = a
        a = b
        b = temp + b


# Here 'factor' signifies the multiplicative factor which expands or
# shrinks the scale of the plot by a certain factor.
factor = 1

n = int(input('Enter the number of iterations (must be > 1): '))

if n > 0:
    # Plotting the Fibonacci Spiral Fractal and printing the corresponding
    # Fibonacci Number
    print("Fibonacci series for", n, "elements :")
    x = turtle.Turtle()
    x.speed(100)
    plotting_fibonacci(n)
    turtle.done()
else:
    print("Number of iterations must be > 0")
