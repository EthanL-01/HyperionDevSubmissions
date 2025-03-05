
#Hello Hyperion Dev, and Hello World! This is my first task submission!

#The block below is my pseudocode planning

'''

check if the user is old enough to enter the Belated Bull nightclub
    define the user's age in a variable
    ask for a numerical input from the user to store in that variable

if the user's input age is >= 18
    tell the user "Access Granted"

if the user's input age is < 18
    tell the user "Access Denied"

'''

#I've a little experience learning Python with SoloLearn, and this is a demonstration of how I would convert my pseudocode to Python:


    #defines user_age as a variable, and converts it to an integer for use in logical computation
user_age = int(input())

    #checks if the input is greater than or equal to 18 and prints "Access Granted!"
if user_age >= 18:
    print("Access Granted! Welcome to the Belated Bull!")

    #only executes if the input is less than 18 and doesn't execute the above if statement and prints "Access Denied!"
else:
    print("Access Denied! Come back another time!")