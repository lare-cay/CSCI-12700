#Name: Clare Lee
#Email: Clare.Lee94@myhunter.cuny.edu
#Date: September 17, 2019
#This program prints out ASCII code of inputed phrase from user

#Saves user input as "phrase"
phrase = input("Enter a phrase ")

print("In ASCII:")
#prints ascii of each char in phrase
for i in range(len(phrase)):
    print(ord(phrase[i]))
               
               
