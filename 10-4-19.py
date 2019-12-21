#Name: Clare Lee
#Email: Clare.Lee94@myhunter.cuny.edu
#Date: October 4, 2019
#This program asks user for a message and print it triplicate

message = input("Enter a message: ")
print()
for i in range(len(message)):
    print(message[i], message[i],  message[i])
