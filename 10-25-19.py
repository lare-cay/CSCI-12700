#Name: Clare Lee
#Email: Clare.Lee94@myhunter.cuny.edu
#Date: October 25, 2019
#This program double the recipe of a user given recipe

import panda as pd

recipe = input("Enter recipe name: ")

#read file and save as df(data frame)
df = pd.read_csv(recipe)

print(df.head())
print(float(df.["Amount"])*2,df.["Measurement"],df.["Ingredient"])
