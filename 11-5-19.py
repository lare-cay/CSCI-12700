#Name: Clare Lee
#Email: Clare.Lee94@myhunter.cuny.edu
#Date: November 5, 2019
#This program takes a binary number and prints out the corresponding decimal numver

#Ask user for input, and store in the string, binString.
#    Set decNum = 0.
#    For each c in binString,
#        decNum = decNum * 2
#        if c is 1, then
#            decNum = decNum + 1
#    Print decNum

binString = input("Enter binary number: ")
decNum = 0
for c in range(len(binString)):
    decNum = decNum * 2
    if binString[c] == "1":
        decNum = decNum +1

    print (decNum)
