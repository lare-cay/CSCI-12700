#Name: Clare Lee
#Email: Clare.Lee94@myhunter.cuny.edu
#Date: October 7, 2019
#This program asks for a list of names and prints out the names in different format

names_string = input("Please enter your list of names: ")
names_list = names_string.split("; ")

print()
print("You entered: ")
print()

for i in range(len(names_list)):
    person = names_list[i].split(", ")
    last_initial = person[1][0] + "."
    print(last_initial, person[0]) 

print()
print("Thank you for using my name organizer!")
