#Name: Clare Lee
#Email: Clare.Lee94@myhunter.cuny.edu
#Date: October 28, 2019
#This program modifies a given program with user input

import pandas as pd
import matplotlib.pyplot as plt

infile = input("Enter name of input file: ")
outfile = input("Enter name of output file: ")

data = pd.read_csv(infile)
data["Fraction Children"] = data["Total Children in Shelter"]/data["Total Individuals in Shelter"] 
data.plot(x = "Date of Census", y = "Fraction Children")
#plt.imsave(outfile, data)
fig = plt.gcf()
fig.savefig(outfile)
