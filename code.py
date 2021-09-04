import turtle
import random
 
t = turtle.Turtle()
screen = turtle.Screen()

moveSpeed = 10
turnSpeed = 10

def moveForward():
  t.pendown()
  t.forward(moveSpeed)

def moveBackward():
  t.pendown()
  t.backward(moveSpeed)
  
def turnLeft():
  t.left(turnSpeed)
  
def turnRight():
  t.right(turnSpeed)
  
t.goto(0,0)

screen.onkey(moveForward, "Up")
screen.onkey(moveBackward, "Down")
screen.onkey(turnLeft, "Left")
screen.onkey(turnRight, "Right")
screen.listen()


