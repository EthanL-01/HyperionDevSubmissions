'''
Pseudocode:

Define three variables called: num1, num2 and num3
	Request input for each and cast them to integers

Define num_sum
	Take each of the three numX variables and store the sum

Print num_sum to display the total of each input
	Cast num_sum to a string

Define num_minus 
	Use this to subtract num2 from num1

Print num_minus
	Cast num_minus to a string
	
Define num_multiply
	Use this to multiply num3 by num1

Print num_multiply
	Cast num_multiply to a string

Define num_sum_divide
	Use this to take the previously defined input total in num_sum
	and divide it by num3

Print num_sum_divide
	Cast num_sum_divide to a string
	
'''

# Defines variables for three inputs
num1 = int(input("Input 1: "))
num2 = int(input("Input 2: "))
num3 = int(input("Input 3: "))

# Totals each input together and stores it in a new variable called num_sum
num_sum = num1 + num2 + num3

# Prints an empty line for formatting
print()
# Casts num_sum to a string and prints it
print ("Total sum: " + str(num_sum))

# Subtracts num2 from num1 and stores it in a new variable called num_minus
num_minus = num1 - num2

# Uses an f-string to insert the relevant variables into the string output, 
# casts num_minus to a string and prints
print(f"{num1} - {num2} = " + str(num_minus))

# Multiplies num3 by num1 and stores it in a new variable called num_multiply
num_multiply = num3 * num1

# Uses an f-string to insert the relevant variables into the string output, 
# casts num_multiply to a string and prints
print(f"{num3} * {num1} = " + str(num_multiply))

# Divides num_sum by num3 and stores it in a new variable called 
# num_sum_divide
num_sum_divide = num_sum / num3

# Uses an f-string to insert the relevant variables into the string output, 
# casts num_sum_divide to a string and prints
print(f"{num_sum} / {num3} = " + str(num_sum_divide))
