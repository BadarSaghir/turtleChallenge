# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings
from shape import Shapes

draw = Shapes()
# draw.makeSquare(100, "turtle")
# draw.dot_lines(200, "turtle")

# draw.pentagon()
for i in range(3, 50):
    draw.shapes(i, 30)

draw.done()
