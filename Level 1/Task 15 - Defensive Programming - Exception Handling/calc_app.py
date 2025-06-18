'''
Pseudocode:

Initialize a Try/Except function that handles opening the equations.txt
file, and ending the program when it cannot find the file

Initialize an idential Try/Except function that handles importing functions
from calc_app_functions.py

Define a list of the four valid operators

Define functions for calculating with each mathematical operator

    Allow user_input_list as an argument

    Declare variables for each of the two list items in user_input_split

    Declare an output variable (eg. division_output) and calculate the two
    list item variables against one another for the output value

    Return the output variable

Move those user defined functions and operator list to calc_app_functions.py 
for cleaner code

Initialize a while loop with a nested Try/Except function which
will handle input validation inside the loop, and loops back for input when
it encounters an error

    Request input equation and store it in a variable called user_input

    Initialize an if/elif/else statement which detects the mathematical
    operator used in user_input_list and executes it's associated user defined
    function

        To verify:
        If no valid operator is detected in the [1] spot it prints an
        appropriate error and loops to requesting input

        To End:
        If the user inputs "end" the loop will break

        To Solve:
        The appropriate if statement will execute based on the operator
        detected in user_input_list, which runs the associated user defined
        function (eg. addition_function) through the output variable and
        prints the output variable

        To Save:
        .write() the user inputs and grammatical formatting to a line in
        equations.txt. Cast the output variable to a string and write it
        and a newline to equations.txt

Set the document "pointer" back to the start of equations.txt with
equations.seek(), then make a final variable to store the contents of
equations.txt for printing called equations_end

Print equations_end

Close equations.txt

Reopen equations.txt with "w" and immediately close, to wipe the file for
future use

'''
# Handles errors involving opening the file
try:
    equations = open("equations.txt", "r+")
except FileNotFoundError as error:
    print("File cannot be found.")
    print(error)
    exit()
except Exception as error:
    print("An unexpected error has occured.")
    print(error)
    exit()

# Handles errors involving importing functions
try:
    from calc_app_functions import (addition_function, subtraction_function,
                                    division_function, multiplication_function, 
                                    operator_list)
except Exception as error:
    print("An unexpected error has occured.")
    print(error)
    exit()

while True:
    # Handles invalid input errors
    try:
        print("Input 'END' to print all results.")
        print("Input calculation individually: (number, then operator, " \
        "then number)")

        # Collects inputs and stores them for referencing
        user_input = input("Input: ").lower()

        # Ends the loop
        if "end" in user_input:
            break

        user_input2 = input("Input: ")
        user_input3 = input("Input: ")

        # Converts inputs into a list
        user_input_list = [user_input, user_input2, user_input3]

        # Handles input validation for invalid operators
        if user_input_list[1] not in operator_list:
            print(f"Invalid operator: {user_input_list[1]}\n")

        # Executes the correct function based on the operator
        elif "+" in user_input_list:
            addition_output = addition_function(user_input_list)
            # Prints the result
            print(f"Result: = {addition_output}\n")
            # Writes the input equation and result to equations.txt
            equations.write(user_input + " " + user_input2 + " "
                            + user_input3 + " " + "=" + " ")
            equations.write(str(addition_output))
            equations.write("\n")

        elif "-" in user_input_list:
            subtraction_output = subtraction_function(user_input_list)
            print(f"Result: = {subtraction_output}\n")
            equations.write(user_input + " " + user_input2 + " "
                            + user_input3 + " " + "=" + " ")
            equations.write(str(subtraction_output))
            equations.write("\n")

        elif "/" in user_input_list:
            division_output = division_function(user_input_list)
            print(f"Result: = {division_output}\n")
            equations.write(user_input + " " + user_input2 + " "
                            + user_input3 + " " + "=" + " ")
            equations.write(str(division_output))
            equations.write("\n")

        elif "*" in user_input_list:
            multiplication_output = multiplication_function(user_input_list)
            print(f"Result: = {multiplication_output}\n")
            equations.write(user_input + " " + user_input2 + " "
                            + user_input3 + " " + "=" + " ")
            equations.write(str(multiplication_output))
            equations.write("\n")

        # Generic error catch
        else:
            print("")
            print("Unexpected error. Please try again.\n")

    # Exception handling to enable the try statement
    except Exception:
        print("")
        print("Unexpected error. Please try again.\n")
        continue

# Sets the pointer back at the start of the file
equations.seek(0)
# Stores the contents of equations.txt for printing
equations_end = equations.read()

# Prints results
print("\nYour Results:")
print(equations_end)

# Closes the file
equations.close()

# Handles wiping the file for future use
open("equations.txt", "w").close()

print(end - start)

