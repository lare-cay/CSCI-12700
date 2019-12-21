#Name: Clare Lee
#Email: Clare.Lee94@myhunter.cuny.edu
#Date: September 19, 2019
#This program takes prompted DNA string and prints the its length and GC content

#prompt and save user dna string 
dna = input("Enter a DNA string: ")

print("Length is ", len(dna))

#count G and C in string and calculate percent GC
GC_count = dna.count("G") + dna.count("C")
percent = GC_count/len(dna)

#print percent of GC in string
print("GC- content is ", round(percent,2))
