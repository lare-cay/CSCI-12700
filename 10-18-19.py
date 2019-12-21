#Name: Clare Lee
#Email: Clare.Lee94@myhunter.cuny.edu
#Date: October 18, 2019
#This program asks users for a borough and file name and then displays the pop. of given borough

#import necessary libraries
import matplotlib.pyplot as plt
import pandas as pd

#ask and save user inputed variables for borough and file name
borough = input("Enter borough name: ")
file_name = input("Enter output file name: ")

#open NYC historical population data and store in "pop"
pop = pd.read_csv('nycHistPop.csv',skiprows=5)

#plot graph
pop["Fraction"] = pop[borough]/pop["Total"]
pop.plot(x= "Year", y= "Fraction")

#save file and store figure under given name
fig = plt.gcf()
fig.savefig(file_name)

