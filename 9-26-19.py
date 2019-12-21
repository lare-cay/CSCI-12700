#Name: Clare Lee
#Email: Clare.Lee94@myhunter.cuny.edu
#Date: September 26, 2019
#This program modifies NYC floodmap

import numpy as np
import matplotlib.pyplot as plt

#Read in the data to an array, called elevations:
elevations = np.loadtxt('elevationsNYC.txt')

#Take the shape (dimensions) of the elevations
#  and add another dimension to hold the 3 color channels:
mapShape = elevations.shape + (3,)

#Create a blank image that's all zeros:
floodMap = np.zeros(mapShape)

for row in range(mapShape[0]):
    for col in range(mapShape[1]):
        #Below sea level
        if elevations[row,col] <= 0:
           floodMap[row,col,2] = 1.0     #Set the blue channel to 50%
        #Below the storm surge of Hurricane Sandy (flooding likely)
        elif elevations[row,col] <= 6:   
            floodMap[row,col,0] = 1.0     #Set the red channel to 50%
        #Below 20 ft above and greater than 6 ft
        elif elevations[row,col] <= 20:
            floodMap[row,col,0] = 0.5
            floodMap[row,col,1] = 0.5
            floodMap[row,col,2] = 0.5
        #Greater than 20 ft above sea level
        else:
            floodMap[row,col,1] = 1.0   #Set the green channel to 50%

#Load the flood map image into matplotlib.pyplot:
plt.imshow(floodMap)

#Save the image:
plt.imsave('floodMap.png', floodMap)
