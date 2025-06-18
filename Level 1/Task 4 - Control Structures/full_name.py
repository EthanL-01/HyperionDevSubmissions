'''
Pseudocode:

Define a variable called full_name and cast to a string

Define a variable called full_name_bool as True

Write an if statement 
	Check if full_name 's character length is equal to 0
	Prints a message if True
	Then sets full_name_bool 's value to False

Write an elif statement
	Check if full_name 's character length is less than 4
	Prints a message if True
	Then sets full_name_bool 's value to False
	
Write a second elif statement
	Check if full_name 's character length is greater than 25
	Prints a message if True
	Then sets full_name_bool 's value to False
	
Write a else statment
	Check if full_name_bool is equal to True
	Prints a message thanking the user for inputting their full name if True

'''
# Defines variables for input and a bool to track through the if statements
full_name = str(input("What is your Full Name? "))
full_name_bool = True

# Checks if the user input nothing, prints a message, and sets 
# full_name_bool to False
if len(full_name) == 0:
    print("You haven't entered anything.")
    print("Please enter your full name.")
    full_name_bool = False

# Checks if the user input less than 4 characters, prints a message, and
# sets full_name_bool to False
elif len(full_name) < 4:
    full_name_bool = False
    print("You have entered less than 4 characters.")
    print("Please make sure that you have entered your name and surname.")

# Checks if the user input more than 25 characters, prints a message, and
# sets full_name_bool to False
elif len(full_name) > 25:
    full_name_bool = False
    print("You have entered more than 25 characters.")
    print("Please make sure that you have entered only your full name.")

# Checks if full_name_bool is still True after the previous if statement, 
# then prints a message
else:
    full_name_bool == True
    print("Thank you for entering your full name.")
    
# I removed the block checking if full_name_bool returns a False value
# as this was redundant