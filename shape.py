from turtle import Turtle, Screen
import  random
color = ["silver", "light cyan", "pale turquoise", "mint cream", "light salmon", "medium purple",
         "linen", "linen", "misty rose", "khaki"
         ]


def turn(make_square, size):
    make_square.forward(size)
    make_square.left(90)


class Shapes:
    def __init__(self):
        self.draw = Turtle()

    def done(self):
        screen = Screen()
        screen.exitonclick()

    def makeSquare(self, size, shape):
        draw = self.draw
        draw.shape(shape)
        for _ in range(4):
            turn(draw, size)

    def dot_lines(self, length, shape):
        draw = self.draw
        draw.shape(shape)
        for i in range(0, length, int(10)):
            draw.down()
            draw.forward(10)
            draw.up()
            draw.forward(10)

    def shapes(self, sides, size):
        shape = self.draw
        shape.color(color[random.randrange(0, len(color))])
        for _ in range(sides):
            shape.forward(size)
            shape.right(360 / sides)

    def rotation(self, teta):
        move = self.draw
        move.right(teta)
