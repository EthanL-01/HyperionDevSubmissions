'''
Pseudocode:

Define variables which request input for the following:
    Name
    Age
    House Number
    Street name

Print each variable in a single grammatically correct string
    Include functions to: 
        Capitalize each section of their name
        Lowercase their age in case they input text
        Lowercase their house number in case they input text
        Capitalize each section of their street name

'''
#defines each variable and prompts the user for input
user_name = input("What is your name? ")
user_age = input("What is your age? " )
user_house_number = input("What is your house number? ")
user_street_name = input("What is your street name? ")

#outputs each variable in a grammatically correct string
#includes functions to appropriately capitalize and 
# lowercase each variable to remain grammatically consistent
print(
    f"This is {user_name.title()}.",
    f"They are {user_age.lower()} years old.",
    f"They live at house number {user_house_number.lower()},", 
    f"on {user_street_name.title()}.",
    # Following review, I've added the sep="\n" escape sequence
    # to the print() function. This tells the print function to                          
    # "separate" each item with a new line (10/03/25)
    sep="\n"
    )