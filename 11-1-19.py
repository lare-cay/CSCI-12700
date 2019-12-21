#Name: Clare Lee
#Email: Clare.Lee94@myhunter.cuny.edu
#Date: November 1, 2019
#This program modifies a parking ticket program


#Import pandas for reading and analyzing CSV data:
import pandas as pd

file_name = input("Enter file name: ")
attribute = input("Enter attribute: ")
tickets = pd.read_csv(file_name)     #Read in the file to a dataframe
print("The 10 worst offenders are:")
print(tickets[attribute].value_counts()[:10]) #Print out the dataframe
