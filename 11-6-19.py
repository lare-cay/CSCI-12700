#Name: Clare Lee
#Email: Clare.Lee94@myhunter.cuny.edu
#Date: November 6, 2019
#This program takes a num 0 - 9 and return the corresponding number as a string

def num2string(num):
    if num == 0:
        numString = "zero"
    if num == 1:
        numString = "one"
    if num == 2:
        numString = "two"    
    if num == 3:
        numString = "three"
    if num == 4:
        numString = "four"
    if num == 5:
        numString = "five"
    if num == 6:
        numString = "six"
    if num == 7:
        numString = "seven"
    if num == 8:
        numString = "eight"
    if num == 9:
        numString = "nine"
    return(numString)


def main():
     nums = input('Enter a multi-digit number: ')
     newStr = ""
     for n in nums:
         word = num2string(int(n))
         newStr = newStr + " " + word
     msg = 'In words, your number is:' + newStr + "."
     print(msg)   


#Allow script to be run directly:
if __name__ == "__main__":
     main()
