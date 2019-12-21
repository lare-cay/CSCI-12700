#Name: Clare Lee
#Email: Clare.Lee94@myhunter.cuny.edu
#Date: September 11, 2019
#This program implements given pseudocode

import turtle

#create window
window = turtle.Screen()

#create turtle 
#set line size
tim = turtle.Turtle()
tim.pensize(5)

#in a for loop repeat given direction 36 times and exits window upon click
for i in range(36):
    tim.forward(100)
    tim.left(55)
    tim.forward(10)
    tim.left(55)
    tim.forward(100)
window.exitonclick()  
