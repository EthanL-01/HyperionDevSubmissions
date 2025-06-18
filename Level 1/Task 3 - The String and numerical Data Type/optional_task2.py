'''
Pseudcode:

Define the following variables which each prompt an input:
	string_fav 
		to store the user's favourite restaurant
	int_fav 
		to store the user's favourite number
		
Print each variable on separate lines

Attempt to cast string_fav to an integer

Print string_fav, which results in an error

'''

# Stores the user's inputs in relevant variables and casts them to their 
# appropriate data types
string_fav = str(input("What is your favourite restaurant? "))
int_fav = int(input("What is your favourite number? "))

# Prints each previously defined variable
print()
print(f"Your favourite restaurant is {string_fav}")
print(f"Your favourite number is {int_fav}")

# Comment out the two lines of code below to properly run the code

# Attempts to cast a string of characters to an integer which results in an 
# error, as an integer can only be numbers
string_fav = int(string_fav)

# Attempts to print string_fav, but as an error occurs earlier in the code
# it will not reach the print() function
print(string_fav)

