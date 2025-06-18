# Let's make some mistakes!

'''
Pseudocode:

Declare a variable called sunrise as False

Open a while statement that executes while sunrise is False
    Declare a variable called hour which requests input and casts to an int

    Open an if statement that checks if the input for hour is less than 0, 
    or greater than 24, and prints a string asking for a valid input, 
    then continues the while statement

    Open an if statement that executes if the input for hour is between 0
    and 24, then declares a variable called hours_until and subtracts hours 
    from 8, calculating the time left until sunrise (8am), and prints a string
    containing hours_until explaining how long is left until sunrise

    Follow on with an elif statement that checks if the input for hour is
    equal to 8, then prints a string explaining it is sunrise and updates
    sunrise to equal True

    Conclude with an else statement that only executes when the input for 
    hour is greater than 8, which declares a variable called hours_since, 
    which subtracts 8 from hours and, prints a string containing hours_since
    explaining how long ago sunrise was and updates sunrise to equal True
'''

# Declares sunrise as False
sunrise = False

# Runs while sunrise == False
## Debug: hour is mispelled as Hour (Syntax Error)
while sunrise is False:
    # Declares hour and requests input
    Hour = int(input("What is the time? "))

    # Executes if the hour input is < 0 or > 24
    if hour < 8 or hour > 24:
        print("Please enter a valid hour between 0 and 24")
        continue
    ## Debug: The less than operator should be checking for < 0
        ##    Entering a value less than 8 returns the wrong value
        ##    (Runtime error)

    # Executes if hour is < 8
    if hour < 8
        # Declares hours_until and subtracts 8 from hour, then prints
        hours_until = 8 - hour
        print (f"Sunrise isn't for {hours_until} hours")
    ## Debug: The if statement is missing colon (Syntax Error)

    # Executes if hour is equal to 8
    elif hour == 8:
        # Prints a string, then updates sunrise to equal True
        print("It's sunrise!")
        sunrise = True

    # Executes when a value greater than 8 is input
    else:
        # Declares hours_since and subtracts the value of hour from 8,
        # then prints and updates sunrise to equal True
        hours_since = hour - 8
        print (f"Sunrise is in {hours_since} hours")
        sunrise = True
        ## Debug: String doesn't reflect this output is actually how many
        ##        hours it has been since sunrise (Logical Error)
