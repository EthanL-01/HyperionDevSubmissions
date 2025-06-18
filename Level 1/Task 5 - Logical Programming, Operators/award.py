'''
Pseudocode:

Print a message stating "You have completed the triathalon."

Define variables that prompt the user for input for the following:
	swimming_time
	cycling_time
	running_time
Cast each of these to integers for computation

Define a variable for total_time which sums up each of the x_time variables

Define a list called awards, which contains the following:
	No Award
	Provincial Scroll
	Provincial Half Colours
	Provincial Colours
	
Write an if-statement which checks the value stored in total_time against a
comparison operator and proceeds to the relevant section of the if-statement
	Prints a message containing the associated value stored in awards

Print the value of total_time

'''

print("You have completed the triathalon.")

# Defines variables for input for each stage of the triathalon
swimming_time = int(input("In minutes, how long did you take to complete "
                        "the swimming stage of the triathalon?\n"))

cycling_time = int(input("In minutes, how long did you take to complete "
                         "the cycling stage of the triathalon?\n"))

running_time = int(input("In minutes, how long did you take to complete "
                         "the running stage of the triathalon?\n"))

# Defines a variable to sum each stage of the triathalon
total_time = swimming_time + cycling_time + running_time

# Defines a list containing each possible award
awards = ["No Award","Provincial Scroll","Provincial Half Colours",
          "Provincial Colours"]

# Checks the value stored in total_time and executes the relevant code
# Prints a message containing their award
if (total_time > 110):
    print(f"\nYour award: {awards [:1]}")

elif (total_time <= 110) and (total_time > 105):
    print(f"\nYour award: {awards [1:2]}")

elif (total_time <= 105) and (total_time > 100):
    print(f"\nYour award: {awards [2:3]}")

else:
    print(f"\nYour award: {awards [3:]}")

# Prints a message containing the value stored in total_time
print(f"Total time: {total_time} minutes")

