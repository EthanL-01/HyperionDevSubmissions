def list_collection (sum_list):
    """Collects inputs to make a list.
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

def int_max (sum_list, max_output):
    """Handles calculating the max integer in a list.
    """
    # Recursively checks through the list, copying the value of that integer
    # then removing it from the list until the list is empty, which then
    # triggers the error handling exception to break the recursive loop
    try:
        if max_output < sum_list[0]:
            max_output = sum_list[0]
            sum_list.pop(0)
            return int_max(sum_list, max_output)
    except IndexError:
        return max_output


# Initializes the list for modifying
sum_list = []
max_output = 0

print("Input each integer in your list individually.")
print("Enter \"=\" to end.\n")

# Prompts the user for input to creat their list of integers
list_collection(sum_list)

# Orders the list numerically
sum_list.sort()

# Finds the largest integer in sum_list
max_output = int_max(sum_list, max_output)

# Prints both the integer list and the largest integer
print(f"\nInteger list: {sum_list}")
print(f"Largest integer: {max_output}")
