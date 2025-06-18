'''
Pseudocode:

Define the following variables for tracking values during the while loop:
	user_num
	num_sum
	num_counter

Print an opening string with instructions explaining that inputting -1 will
end the while loop

Write a while loop which exits the loop when the user inputs -1
	Prompt the user for input to user_num and cast it to a float
	Follow with an if statement which executes if the input doesn't equal -1
	    Update num_sum adding user_num
	    Update num_counter by 1
	
Define a variable called num_mean
	Assign a value to num_mean by dividing num_sum by num_counter
	
Print strings containing num_sum and num_mean
'''

# Defines variables for tracking values during the while loop
user_num = 0
num_sum = 0
num_counter = 0

# Prints an opening statement with instructions
print("Enter values to calculate their average, "
      "then enter -1 when you wish to stop.")

# Initializes a while loop, ending when the user inputs -1
while user_num != -1:
    user_num = float(input("\nPlease enter a number: "))
    if user_num != -1:
        num_sum = num_sum + user_num
        num_counter += 1

# Defines a variable for the mean average and calculates this by dividing
# the total of the input numbers by the amount of numbers inputted
num_mean = num_sum / num_counter

# Prints the values stored in num_sum and num_mean
print(f"\nThe total sum is: {num_sum}")
print(f"The mean average is: {num_mean}")
