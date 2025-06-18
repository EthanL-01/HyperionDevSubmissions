'''
This example program is meant to demonstrate errors
There are some errors in this program
Run the program, look at the error messages, and find and fix the errors

'''
# Prints an opening string
print ("\nWelcome to the error program\n")
## Debugged: Added brackets to the print() statement - Syntax Error
## Debugged: Removed unintended indentations (Syntax Error)
## Debugged: Removed the second print statement and included newline commands
##           for formatting

# Variable declaring the user's age and prints the result
age = 24
## Debugged: Removed unintended indentations (Syntax Error)
## Debugged: Updated age_Str from equals to (==) to equals (=) (Syntax Error)
## Debugged: Removed age_Str variable as this was redundant and updated age to
##           a flat integer of 24 (Logical Error)
## Debugged: Removed unnecessary int() casting from age

print(f"I'm {age} years old.")
## Debugged: Updated to an f-string, removed unnecessary quotations
##           marks (Syntax Error)

# Variables declaring additional years
years_from_now = 3
total_years = age + years_from_now
## Debugged: Removed unintended indentations (Syntax Error)
## Debugged: Removed quotation marks from years_from_now to allow for
##           computation (Syntax Error)

# Prints the total years of age
print (f"In three years, I will be: {total_years}")
## Debugged: Updated to an f-string and changed answer_years to total_years
##           (Syntax Error)
## Debugged: Updated string text to reflect the given value (Logical Error)

# Variable to calculate the total amount of months from the total amount of
# years and prints the result
total_months = total_years * 12 + 6
print (f"In 3 years and 6 months, I'll be: {total_months} months old")
## Debugged: Updated total to total_years to allow for computation
##           (Syntax Error)
## Debugged: Updated total_months to addition the extra 6 months
##           (Logical Error)
## Debugged: Added parenthesis to the print function and updated to an
##           f-string (Syntax Error)

#HINT, 330 months is the correct answer
