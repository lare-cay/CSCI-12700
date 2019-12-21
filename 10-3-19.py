#Name: Clare Lee
#Email: Clare.Lee94@myhunter.cuny.edu
#Date: October 3, 2019
#This program asks for 5 whole numbers and moves turtle according to those numbers

numArray = []
for i in range(5):
    num = int(input("Enter a number: "))
    numArray.append(num)

import turtle
tom = turtle.Turtle()

for i in numArray:
    tom.left(i)
    tom.forward(100)
