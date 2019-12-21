#Name: Clare Lee
#Email: Clare.Lee94@myhunter.cuny.edu
#Date: September 9, 2019
#This program prints: an octagon w/ turtle

import turtle

#create window and background color
window = turtle.Screen()
window.bgcolor("skyblue")

#create turtle named tim
#set tim's shape, color, and line size
tim = turtle.Turtle()
tim.shape("turtle")
tim.color("forestgreen")
tim.pensize(5)

#create a loop so tim creats a octagon and exits window on click
for i in range(8):
    tim.forward(50)
    tim.stamp()
    tim.left(45)
window.exitonclick()  
