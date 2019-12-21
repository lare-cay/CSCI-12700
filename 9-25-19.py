#Name: Clare Lee
#Email: Clare.Lee94@myhunter.cuny.edu
#Date: September 25, 2019
#This program creates a C logo on 30 x 30 grid

#import libraries for plotting and arrays
import matplotlib.pyplot as plt 
import numpy as np

#create grid with 3 sheets of 1's
logo = np.ones((30,30,3))
#turn left 10 out of 30 columns blue by turing red and green to 0
logo[:,:10,0] = 0
logo[:,:10,1] = 0
#turn top 10 and bottom 10 rows blue by turing red and green to 0
logo[:10,:,0] = 0
logo[:10,:,1] = 0
logo[:-10,:,0] = 0
logo[:-10,:,1] = 0

#save logo array to file
plt.imsave("logo.png", logo)
