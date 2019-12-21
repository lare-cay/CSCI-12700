#Name: Clare Lee
#Email: Clare.Lee94@myhunter.cuny.edu
#Date: October 21, 2019
#This program computes min,avg,max of population for user entered borough

import pandas as pd

borough = input("Enter borough: ")

pop = pd.read_csv('nycHistPop.csv',skiprows=5)
print("Minimum population", pop[borough].min())
print("Average population", pop[borough].mean())
print("Maximum population", pop[borough].max())
