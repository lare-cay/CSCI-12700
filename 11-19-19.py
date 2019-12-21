#Name: Clare Lee
#Email: Clare.Lee94@myhunter.cuny.edu
#Date: November 19, 2019
#This program modifies lab 9 program

import turtle
import random

trey = turtle.Turtle()
trey.speed(10)

for i in range(100):
  trey.forward(30)
  a = random.randrange(0,360,10)
  trey.right(a)
