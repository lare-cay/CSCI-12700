#Name: Clare Lee
#Email: Clare.Lee94@myhunter.cuny.edu
#Date: September 20, 2019
#This program prints out a new sentence from user inputed noun and two verbs

#store sentence template as a variable
template = "If it VERB1 like a NOUN and VERB2 like a NOUN, it probably is a NOUN."

#ask user for noun and store as variable
#replace noun in template with user input
noun = input("Enter a noun: ")
template = template.replace("NOUN", noun)
#ask user for verb1 and store as variable
#replace verb1 in template with user input
verb1 = input("Enter a verb: ")
template = template.replace("VERB1", verb1)
#ask user for verb2 and store as variable
#replace verb2 in template with user input
verb2 = input("Enter another verb: ")
template = template.replace("VERB2", verb2)

#print new sentence
print("New sentence:")
print(template)
      
