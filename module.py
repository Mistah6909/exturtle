
import turtle
import random
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
    turtle.setheading(90)
    for x in range(dimension):
      turtle.left(90)
      turtle.forward(size)
      turtle.right(90)
      turtle.forward(size)
      turtle.right(90)
      turtle.forward(size)
      turtle.right(90)
      turtle.forward(size)
      turtle.right(90)
      turtle.forward(size)
      turtle.right(90)
      turtle.forward(size)
      size = size/1.8
  def change_color(color):
    turtle.color(color)
  def clear(self):
    turtle.clear()
  def set_pos(self,x,y):
    turtle.pen("up")
    turtle.setposition(x,y)
  def rng(self,times,direction = 0,rng_direction = 0):
    for x in range(times):
      turtle.forward(random.randint(1,100))
      if direction == 0:
        rng_direction = random.randint(0,3)
      if rng_direction == 1:
        turtle.left(random.randint(0,361))
      if rng_direction == 2:
        turtle.left(random.randint(0,361))
      if direction > rng_direction:
        rng_direction = 3
  def speed(self,speed):
    turtle.speed(speed)
      
  def polygon(self,sides,side_length,angle = 0):
    angle = (sides-2) * 180
    angle = angle / sides
    return angle
    turtle.forward(side_length)
    turtle.right(180-angle)
