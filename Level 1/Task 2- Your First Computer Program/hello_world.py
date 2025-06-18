'''
Pseudocode:

Define a variable for storing the user's name
    Request input for this variable

Define a variable for storing the user's age
    Request input for this variable

Print the user's name 
Print the user's age 
Print the statement "Hello World!"
Include functions to appropriately capitalize and lowercase each variable to remain grammatically consistent

'''
#defines the variable user_name and prompts the user for an input value
user_name = input("What is your name? ")

#defines the variable user_age and prompts the user for an input value
user_age = input("What is your age? ")

#prints and concatenates the associated text and the now-defined variables
    #includes functions to capitalize each output appropriately to remain grammatically consistent
print("Name: " + user_name.title())
print("Age: " + user_age.capitalize())

#prints an additional statement at the end of the program
print("Hello World!")