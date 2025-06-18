# Takes user input for the if loop to follow
user_input = input("Is there an energy drink in the fridge? (Yes/No) ")

# Uses user input to update check_fridge boolean
if user_input == "Yes":
    check_fridge = False
elif user_input == "No":
    check_fridge = True
else:
    check_fridge = None
    print("Invalid input")
## Debug: Boolean values are flipped and will cause an incorrect
##        print output (Logical Error)

# Checks check_fridge and prints an appropriate message
if check_fridge == True:
    print("No need to go to the supermarket")

elif check_fridge != True:
    print("Time to go to the supermarket")

else:
    print("Please try again")
