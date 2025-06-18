''''
This example program is meant to demonstrate errors.

There are some errors in this program. Run the program, look at the 
error messages, and find and fix the errors.
'''
# Declares variables
animal = "Lion"
animal_type = "cub"
number_of_teeth = 16
## Debugged: Added quotation marks to animal to define it as a string
##           (Syntax error)

# Declares variable as an f-string
full_spec = (f"\nThis is a {animal}. It is a {animal_type} " \
            f"and it has {number_of_teeth} teeth.")
## Debugged: Split the string across two lines to adhere to character
##           limit guidelines (Syntax / Formatting error)
## Debugged: Updated to an f-string (Syntax / Formatting error)
## Debugged: Swapped number_of_teeth and animal_type around (Logical error)
## Debugged: Added a newline command to the string for formatting
##           (Syntax/Formatting error)

# Prints full_spec
print (full_spec)
## Debugged: Added parenthesis to the print statement (Syntax error)
