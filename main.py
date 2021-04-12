import turtle
import random
'''
5. pen features
  penup
  variable1.penup()

  pendown
  variable1.pendown()

  move to point
  variable1.goto(x,y)

  move to origin
  variable1.home()

  color
  variable1.color(COLOR)

  shape
  variable1.shape(SHAPE)

  speed
  variable1.speed(NUMBER)

  write
  variable1.write(TEXT,MOVE,ALIGN,FONT)
  FONT = (FONTTYPE, FONTSIZE, FONTSTYLE)

  width
  variable1.width(NUMBER)

  circle
  variable1.circle(RADIUS)
  variable1.circle(RADIUS, ANGLE)
  variable1.circle(RADIUS, ANGLE, SIDE)

  fill color
  variable1.fill("COLOR")

  variable1.begin_fill()

  variable1.end_fill()

'''
pen = turtle.Turtle()

''''
# Exercise 1 - Draw a Star
def drawStar(l):
  for i in range(5):
    pen.forward(l)
    pen.right(144)

  drawStar(int(input("LENGTH : ")))
'''
'''
# Exercise 2 - Drawing Shapes
def drawShape(r,s):
  pen.circle(r,360,s)
drawShape(float(input("Radius: ")), int(input("Number of Sides: ")))
'''

# Exercise 3 - Draw A Spiral
# List color
colors = ["yellow","pink","red","orange","green","blue"]
# For Loop
for x in range(50):
  pen.color(colors[x % 6])
  pen.width(x / 5 + 1)
  pen.forward(x)
  pen.left(20)