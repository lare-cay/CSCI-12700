#Name: Clare Lee
#Email: Clare.Lee94@myhunter.cuny.edu
#Date: September 18, 2019
#This program ciphers prompted phrase

#prompts user for a word
word = input("Enter a word: ")

#create new variable for ciphered word(cword)
cword = ""
print("Your word in code is:")
#ciphers word and then prints it
for i in range(len(word)):
    #finds how many letters past "a"
    change = ord(word[i])- ord("a") + 13
    #if next letters is beyond "z" continues from "a" again
    wrap = change % 26
    #creates ciphered letter
    letter = chr(ord("a") + wrap) 
    #adds ciphered word to make cword
    cword = cword + letter 
print(cword)
