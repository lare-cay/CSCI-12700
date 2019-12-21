#Name: Clare Lee
#Email: Clare.Lee94@myhunter.cuny.edu
#Date: October 11, 2019
#This program askas user for a .png file and prints the number of pixels that are nearly white

import matplotlib.pyplot as plt
import numpy as np

file = input("Enter a file name: ")

file_1 = plt.imread(file)   
countSnow = 0           
t = 0.75

for i in range(file_1.shape[0]):
     for j in range(file_1.shape[1]):
          #Check if red, green, and blue are > t:
          if (file_1[i,j,0] > t) and (file_1[i,j,1] > t) and (file_1[i,j,2] > t):
               countSnow = countSnow + 1

print("Snow count is", countSnow)
