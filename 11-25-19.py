#Name: Clare Lee
#Email: Clare.Lee94@myhunter.cuny.edu
#Date: November 25, 2019
#This program registers $s0 loop 2 - 20

ADDI $s0, $zero, 2 #initial value
ADDI $s1, $zero, 20 #last value
ADDI $s2, $zero, 2 #incrementer
AGAIN: ADDI $s0, $s2, $s0 
BEQ $s0, $s1, DONE #when $s0 is equal to 20 break out of loop
J AGAIN #go to diff part of program
DONE: #breaks out of loop
