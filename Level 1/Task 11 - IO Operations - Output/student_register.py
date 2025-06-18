'''
Write a program that takes name inputs and writes to a new file

Declare a variable for integer inputs that controls the for loop iterations

Write a for loop that references the input integer

Each iteration of the for loop requests a student ID as input and writes 
this and a dotted line after each entry to the new file

Close the file

'''
# Prompts user for input on the number of students
num_students = int(input("How many students are registering? "))

# Creates a file called reg_form.txt and writes to it
form = open("reg_form.txt", "w")

# Prompts user for input for their student ID as many times as is stored 
# in num_students and writes each ID to a new line in reg_form.txt followed 
# by a line break
for i in range (num_students):
        student_id = input("What is your student ID? ")
        form.write(student_id+"\n")
        form.write("....."+"\n")

# Closes the file
form.close()
