#Name: Clare Lee
#Email: Clare.Lee94@myhunter.cuny.edu
#Date: November 20, 2019
#This program asks user for age accepting only a positivem number and print it

num = int(input("Enter your age: "))
while num < 0:
    print("Entered a negative number.")
    num = int(input("Enter your age: "))
print("You enetered your age as: ", num)
