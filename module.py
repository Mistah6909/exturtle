
import turtle
class exturtle:
  def __init__(self,size,color):
    self =  turtle.Turtle()
    self.size =  turtle.shapesize(size)
    self.color = turtle.color(color)
  def move(self,size):
    turtle.forward(size)
  def square(self,size):
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
  def sqrFractal(self,dimension,size):
    #turtle.degree()
    for x in range(dimension):
      turtle.forward(size)
      turtle.right(90)
      turtle.forward(size)
      turtle.right(90)
      turtle.forward(size)
      turtle.right(90)
      turtle.forward(size)
      turtle.right(90)
      turtle.forward(size)
      size = size/1.75
