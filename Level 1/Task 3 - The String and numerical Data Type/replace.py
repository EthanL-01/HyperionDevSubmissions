'''
Pseudocode:

Define a variable called fox_original for the original string:
    "The!quick!brown!fox!jumps!over!the!lazy!dog."

Define additional strings for further iterations of the original string:
    Define variables for the following:
            fox_replace to replace characters
            fox_upper to uppercase characters

Use the .replace() function to replace each ("!") in the fox_original
variable with a space (" ") and store it in the fox_replace variable

Print fox_replace

Use the .upper() function to replace each character in the fox_replace 
variable to uppercase characters and store it in the fox_upper variable

Print fox_upper

Print the fox_upper variable in reverse using string slicing

'''
# Defines a variable for the original string and variables
# for iterations involving replacing and uppercasing characters
fox1 = "The!quick!brown!fox!jumps!over!the!lazy!dog."
fox_replace = fox1.replace("!" , " ")
fox_upper = fox_replace.upper()

# Prints the string and replaces each "!" with a space
print(fox_replace)

# Prints the string and changes each character to uppercase
print(fox_upper)

# Prints the string in reverse using string slicing
print(fox_upper[::-1])