#Name: Clare Lee
#Email: Clare.Lee94@myhunter.cuny.edu
#Date: October 2, 2019
#This program implements given pseudocode

#1.  Ask the user for the number of seconds until lecture starts.
#2.  Print out the hours until lecture (hours = seconds //3600).
#3.  Compute the remaining seconds (rem = seconds % 3600).
#4.  Print out the minutes until lecture (minutes = rem // 60).
#5.  Print out the remaining seconds (remSec = rem % 60).

sec = int(input("INPUT SECONDS BEFORE LECTURE "))



print("Hours: ", sec//3600)
print("Minutes: ", (sec % 3600)//60)
print("Seconds: ", (sec % 3600)% 60)


