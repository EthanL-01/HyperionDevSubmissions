'''
Pseudocode:

Define a string called stars that contains the value: "*"

Write a for loop that will execute 9 times, printing an ascending and then 
descending string of "*" characters
    Nest an if/else statement in the for loop
        The if section will check against the index variable and only run 
        for the first four iterations, printing stars and adding a "*" to 
        the string for the next iteration

        The else statement will execute for iterations 5 and on, printing
        stars and will replace a single "*" character in stars with a blank 
        space for the next iteration

'''

# Defines a variable for the string outputs
stars = "*"

# Initializes a for loop that will run for 9 iterations
for i in range (1, 10):
    # Will only run for the first four iterations when i is less than 5
    if i < 5:
        # Prints the stars variable
        print(stars)
        # Concatenates stars with a "*" character for the next iteration
        stars = stars + "*"

    # Will only run for the last five iterations when i is greater than or
    # equal to 5
    else:
        # Prints the stars variable
        print(stars)
        # Replaces a single "*" character in stars with a blank space
        stars = stars.replace("*", "", 1)
