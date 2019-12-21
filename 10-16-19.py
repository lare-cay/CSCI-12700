#Name: Clare Lee
#Email: Clare.Lee94@myhunter.cuny.edu
#Date: October 16, 2019
#This program modifies a map according to given amount of blue crating a new image

import numpy as np
import matplotlib.pyplot as plt

blue = input("How blue is the ocean: ")
file_name = input("What is the output file: ")

#Read in the data to an array, called elevations:
elevations = np.loadtxt('elevationsNYC.txt')

#Take the shape (dimensions) of the elevations
#  and add another dimension to hold the 3 color channels:
mapShape = elevations.shape + (3,)

#Create a blank image that's all zeros:
blueMap = np.zeros(mapShape)

for row in range(mapShape[0]):
    for col in range(mapShape[1]):
        if elevations[row,col] <= 0:
           blueMap[row,col,2] = blue #Set the blue channel to user specified
        elif elevations[row,col] % 10 == 0:
           blueMap[row,col,0] = 0.0     
           blueMap[row,col,1] = 0.0
           blueMap[row,col,2] = 0.0
        else:
            blueMap[row,col,0] = 1.0
            blueMap[row,col,1] = 1.0
            blueMap[row,col,2] = 1.0

#Save the image:
plt.imsave(file_name, blueMap)

print("Thank you for using my program!")
print("Your map is stored", file_name)
