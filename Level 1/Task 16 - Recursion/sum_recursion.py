def list_collection (sum_list):
    """Recursively collects inputs to make a list.
    """
    user_input = input("Input: ")

    # Handles ending the recursion
    if "=" in user_input:
        return sum_list

    try:
        # Appends the user's input to sum_list and recurs the function
        sum_list.append(int(user_input))
        list_collection(sum_list)

    # Handles input validation and recurs the function
    except ValueError:
        print("Please enter a valid number.")
        return list_collection(sum_list)
    except IndexError:
        print(f"Please enter at least ({index} + 1) integers.")
        return list_collection(sum_list)

def list_addition (sum_list, index):
    """Recursively sums each integer in the list up to and including the 
    provided index number.
    """
    # Handles ending the recursion
    try:
        if index < 0:
            return 0
        # Recursively adds each index number in reverse and returns the sum
        return sum_list[index] + list_addition(sum_list, index -1)
    except IndexError:
        print("Index out of list range.")
        list_collection(sum_list)
        return sum_list[index] + list_addition(sum_list, index -1)

# Initializes variables for modifying
sum_list = []
user_input = None

print("Enter \"=\" to end.")

# Prompts user input for the index value
try:
    index = int(input("Input Index Number: "))
except ValueError:
    index = int(input("Oops Try Again: "))

print("\nInput each integer in your list individually.")
print(f"Enter at least ({index + 1}) integers in total.\n")

# Prompts the user for input and creates a list of integers
list_collection(sum_list)

# Outputs the sum of each number in the list up to and including the index no.
list_output = list_addition(sum_list, index)

print(f"Total sum: {list_output}")
