#Name: Clare Lee
#Email: Clare.Lee94@myhunter.cuny.edu
#Date: November 21, 2019
#This program writes "Hello, World!"

ADDI $sp, $sp, -14
ADDI $t0, $zero, 72 #H
SB $t0, 0($sp)
ADDI $t0, $zero, 101 #e
SB $t0, 1($sp)
ADDI $t0, $zero, 108 #l
SB $t0, 2($sp)
ADDI $t0, $zero, 108 #l
SB $t0, 3($sp)
ADDI $t0, $zero, 111 #o
SB $t0, 4($sp)
ADDI $t0, $zero, 32 #Space
SB $t0, 5($sp)
ADDI $t0, $zero, 44 #,
SB $t0, 6($sp)
ADDI $t0, $zero, 87 #W
SB $t0, 7($sp)
ADDI $t0, $zero, 111 #o
SB $t0, 8($sp)
ADDI $t0, $zero, 114 #r
SB $t0, 9($sp)
ADDI $t0, $zero, 108 #l
SB $t0, 10($sp)
ADDI $t0, $zero, 108 #l
SB $t0, 11($sp)
ADDI $t0, $zero, 100 #d
SB $t0, 12($sp)
ADDI $t0, $zero, 33 #!
SB $t0, 13($sp)

ADDI $v0, $zero, 4
ADDI $a0, $sp, 0
syscall
