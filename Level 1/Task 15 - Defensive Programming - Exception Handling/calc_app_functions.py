# List of operators for input validation referencing
operator_list = ["+", "-", "/", "*"]

# User defined functions to match their defined operator

def addition_function(user_input_list):
    # Handles input validation
    try:
        # Defines variables for each calculable item in the user input list
        calc1 = float(user_input_list[0])
        calc2 = float(user_input_list[2])
        # Defines a variable and stores calculation for output
        addition_output = (calc1 + calc2)
        return addition_output
    # Executes when an invalid input is detected
    except ValueError as error:
        print(f"Invalid input: {error}")
        return error
    except (user_input_list[1]) not in operator_list as error:
        print(f"Invalid operator: {error}")
        return error

def subtraction_function(user_input_list):
    try:
        calc1 = float(user_input_list[0])
        calc2 = float(user_input_list[2])
        subtraction_output = (calc1 - calc2)
        return subtraction_output
    except ValueError as error:
        print(f"Invalid input: {error}")
        return error


def division_function(user_input_list):
    try:
        calc1 = float(user_input_list[0])
        calc2 = float(user_input_list[2])
        division_output = (calc1 / calc2)
        return division_output
    except ValueError as error:
        print(f"Invalid input: {error}")
        return error
    # Executes when a ZeroDivisionError occurs
    except ZeroDivisionError as error:
        print(f"Invalid zero division error: {error}")
        return error
    except (user_input_list[1]) not in operator_list as error:
        print(f"Invalid operator: {error}")
        return error

def multiplication_function(user_input_list):
    try:
        calc1 = float(user_input_list[0])
        calc2 = float(user_input_list[2])
        multiplication_output = (calc1 * calc2)
        return multiplication_output
    except ValueError as error:
        print(f"Invalid input: {error}")
        return error
    except (user_input_list[1]) not in operator_list as error:
        print(f"Invalid operator input")
        return error
