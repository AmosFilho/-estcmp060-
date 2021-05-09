from turtle import *

speed('fastest')
rt(-90)
angle = 30


def fractal_tree(size, level):
    if level > 0:
        colormode(255)

        # Splitting the rgb range for green into equal intervals for
        # each level setting the colour according to the current level
        pencolor(0, 255 // level, 0)

        # Drawing the base
        fd(size)
        rt(angle)

        # Recursive call for the right subtree
        fractal_tree(0.8 * size, level - 1)
        pencolor(0, 255 // level, 0)
        lt(2 * angle)

        # Recursive call for the left subtree
        fractal_tree(0.8 * size, level - 1)
        pencolor(0, 255 // level, 0)
        rt(angle)
        fd(-size)


fractal_tree(80, 7)
