'''
Pseudocode:

Declare the following variables for item stock and prompt user for input
    app_stock, ora_stock, ban_stock, wat_stock

Create a list called menu with the following items and their stock:
    [("apple", 30), ("orange", 20), ("banana", 10), ("watermelon", 5)]

Convert the menu list to a dictioanry

Create a dictionary called price, and assign a price to each item in menu
    apple: 1.00
    orange: 1.25
    banana: 2.00
    watermelon: 3.50

Calculate the total stock value of each item together

Print the total
'''
# Prompts the user for input to detemine stock for each item in menu list
app_stock = int(input("How many apples are in stock? "))
ora_stock = int(input("How many oranges are in stock? "))
ban_stock = int(input("How many bananas are in stock? "))
wat_stock = int(input("How many watermelons are in stock? "))

# Contains a list of tuples of fruit and their associated stock
menu = [("apple", app_stock), ("orange", ora_stock),
        ("banana", ban_stock), ("watermelon", wat_stock)]

# Converts the menu list to a dictionary
stock = dict(menu)

# A dictionary containing the price values for each item
price = {"apple": 1.00,
         "orange": 1.25,
         "banana": 2.00,
         "watermelon": 3.50
        }

# calculates the total price of all the stock stored in menu
total = ((stock["apple"]*price["apple"])+
         (stock["orange"]*price["orange"])+
         (stock["banana"]*price["banana"])+
         (stock["watermelon"]*price["watermelon"])
        )

# Prints the total price of all stock stored in total to two decimals
print(f"\nThe total price of all stock is: £{total:.2f}")
