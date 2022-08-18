import turtle
class exturtle:
  def __init__(self,name,size,color):
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
  def sqrFractal(self,dimension,sqr_size):
    #turtle.degree()
    for x in range(dimension):
      turtle.square(sqr_size)
      turtle.forward()
      sqr_size -= 10


