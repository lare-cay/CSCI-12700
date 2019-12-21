#Name: Clare Lee
#Email: Clare.Lee94@myhunter.cuny.edu
#Date: September 24, 2019
#This program takes inputed image and creates a new image with only the blue channel

#Import the packages for images and arrays
import matplotlib.pyplot as plt
import numpy as np

#ask user for image .png file and name of output file
infile = input("Enter name of the input file: ")
outfile = input("Enter name of the output file: ")
#read image,load to pylot and show image
img = plt.imread(infile)   
plt.imshow(img)		           

#make a copy of image and set non-blue channels to 0
img2 = img.copy()        
img2[:,:,0] = 0          
img2[:,:,1] = 0          

#load new image to pylot and show it
plt.imshow(img2)         
plt.show()

plt.imsave(outfile, img2)  
