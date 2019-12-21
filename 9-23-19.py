#Name: Clare Lee
#Email: Clare.Lee94@myhunter.cuny.edu
#Date: September 23, 2019
#This program demonstrates the shades of blue

#import the turtle library
import turtle				

#allows colors of
turtle.colormode(255)		
tom = turtle.Turtle()		
tom.shape("turtle")		
tom.backward(100)		

#For 0,10,20,...,250
for i in range(0,255,10):
     tom.forward(10)		
     tom.pensize(i)	    
     tom.color(0,0,i)		
