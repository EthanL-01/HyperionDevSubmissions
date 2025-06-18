'''
Pseudocode:

Define a variable called str_manip 
    Prompt the user for input

Define a variable called str_length
    Use the len() function to calculate the string length stored in str_manip
	and store it in the str_length variable

Print str_length to display how many characters are stored in 
the str_length variable

Define a variable called str_manip2

Use string slicing to determine the last character stored in str_manip
and store it in str_manip2

Define a variable called str_manip_replace

Use the replace() function to take the value stored in str_manip2 and
replace each instance of this character in str_manip with an "@" character, 
then store the updated string in the str_manip_replace variable

Print str_manip_replace

Define a new variable called str_manip_end
    Use string slicing to determine the last three characters stored in 
    str_manip, reverse them and then store this in str_manip_end

Print str_manip_end

Define a variable called str_manip_p1
    Use string slicing to determine the first three characters stored in 
    str_manip and store this in str_manip_p1

Define a variable called str_manip_p2
    Use string slicing to determine the last two characters stored in 
    str_manip and store this in str_manip_p2

Print str_manip_p1 and str_manip_p2 to display both variables concatenated
together 

'''

# Requests input from the user and stores it in str_manip
str_manip = input("Input: ")
# Stores the string length of str_manip
str_length = len(str_manip)

# Casts str_length to a string and prints
print("String length: " + str(str_length))

# Uses slicing to identify the last character in str_manip and stores it in 
# str_manip2
str_manip2 = str_manip[-1]

# Prints the value stored in str_manip2
print("Character to be replaced: " + str_manip2)

# Takes the value stored in str_manip2 and replaces each matching character in
# str_manip, then stores this revised string in str_manip_replace
str_manip_replace = str_manip.replace(str_manip2 , "@")

# Prints the revised string stored in str_manip_replace
print("Updated string: " + str_manip_replace)

# Uses slicing to take the last three characters from str_manip and stores 
# them in reverse in str_manip_end
str_manip_end = str_manip[-1:-4:-1]

# Prints the values stored in str_manip_end
print("The last three characters in reverse: " + str_manip_end)

# Uses slicing to take the first three, and the last two characters of 
# str_manip and stores them respectively in str_manip_p1 and str_manip_p2
str_manip_p1 = str_manip[:3]
str_manip_p2 = str_manip[-2:]

# Prints a concatenation of str-manip_p1 and str_manip_p2
print("The first three and last two characters concatenated: " +
      str_manip_p1 + str_manip_p2)

