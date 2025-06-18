'''
Pseudocode:

Import user defined functions from functions.py
    hotel_index
    hotel_cost
    plane_cost
    car_rental
    car_rate
    holiday_cost

Define functions for the following and store them in functions.py:
    hotel_index
        contains a list of destinations and their associated hotel costs
        per night, which is converted to a dictionary called hotel_index
    hotel_cost
        takes num_nights as an argument and returns a total cost
        for their hotel stay
    plane_cost
        takes city_flight as an arguement and returns a total cost
        for their flight
    car_rental
        takes rental_days as an arguement and returns a total cost
        for their car rental
    car_rate
        returns the daily car rental rate based on city_flight
    holiday_cost
        takes hotel_cost, plane_cost and car_rental as arguments 
        and returns a total cost for their holiday

Declare the following variables and request input for each:
    city_flight - The user's city name input
        Initialize an input verification while loop
            Check whether the user's input is in hotel_index

    num_nights - The user's number of nights stayed
        Initialize an input verification while loop
            Write a try/except block statement which verifies that the
            user is inputting an integer

    rental_days - The user's number of days they will rent a car
        Initialize an input verification while loop
            Write a try/except block statement which verifies that the
            user is inputting an integer

Declare the following variables and define them by their associated function:
    hotel_output = hotel_cost(num_nights)
    plane_output = plane_cost(city_flight)
    rental_output = car_rental(rental_days)
    rental_choice = car_rate()
    holiday_output = holiday_cost(hotel_output, plane_output, rental_output)

Print the following outputs to two decimal points:
    Flight Cost
    Hotel Cost (and daily rate)
    Car Rental Cost (and daily rate)
    Total Holiday Cost

'''
# Imports user defined functions stored in functions.py
from functions import hotel_cost, plane_cost, car_rental, car_rate, holiday_cost, hotel_index

# Prompts user for input on where they would like to vacation
city_flight = input("\nWhere would you like to go on holiday? \n"
                    "Please choose from: Coventry, Vilnius, "
                    "Semnan and Tarakan: ").lower()

# Performs a validation check if the user inputs an invalid destiantion
while city_flight not in hotel_index:
    city_flight = input("\nInvalid Selection: \n"
                    "Please choose from: Coventry, Vilnius, "
                    "Semnan and Tarakan: ").lower()

# Prompts the user for input on how many days they are staying and 
# performs a validation check in case they input an invalid number
while True:
    try:
        num_nights = int(input("\nHow many nights will you stay?: "))
        if num_nights >= 0:
            break
    except ValueError:
        print("Invalid selection. Please input a whole number. ")

# Identical to the above operation, instead handling how many days they 
# will rent a car
while True:
    try:
        rental_days = int(input("\nHow many days will you rent a car?: "))
        if rental_days >= 0:
            break
    except ValueError:
        print("Invalid selection. Please input a whole number. ")

# Calculates outputs for printing using each user defined function
hotel_output = hotel_cost(city_flight, num_nights)
plane_output = plane_cost(city_flight)
rental_output = car_rental(city_flight, rental_days)
rental_choice = car_rate(city_flight)
holiday_output = holiday_cost(hotel_output, plane_output, rental_output)

# Prints each output to two decimals
print(f"\nFlight cost: £{plane_output:.2f}")
print(f"Hotel Cost: £{hotel_output:.2f}"
      f" (£{hotel_index[city_flight]:.2f} per day)")
print(f"Car Rental Cost: £{rental_output:.2f}"
      f" (£{rental_choice:.2f} per day)")

print(f"\nTotal holiday cost: £{holiday_output:.2f}")
