#Name: Clare Lee
#Email: Clare.Lee94@myhunter.cuny.edu
#Date: November 8, 2019
#This program modifies program from lab 6

import pandas as pd
import matplotlib.pyplot as plt

#ask the user to specify the input file
#ask the user to specify the output file
inFile = input("Enter name of input file: ")
outFile = input("Enter name of output file: ")

#Convert the date column
df = pd.read_csv(inFile)
df["Date"] = pd.to_datetime(df["Date"].apply(str))

#Make a plot of the percentage of the total population that are children over time from the data in input file
df["% Attending"] = (df["Present"]/df["Enrolled"]) * 100
df.plot(x = "Date", y = "% Attending")

#store the plot in the output file the user specified.
fig = plt.gcf()
fig.savefig(outFile)
