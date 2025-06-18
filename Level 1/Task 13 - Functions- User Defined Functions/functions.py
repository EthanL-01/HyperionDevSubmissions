'''

This file contains my user defined functions, which I can access and 
reference in the main holiday.py file.

I wanted to practice this to make my main code body cleaner.

'''

# Declares hotel_list containing destinations and their nightly hotel rate
hotel_list = [("coventry", 79.99), ("vilnius", 59.99),
            ("semnan", 39.99), ("tarakan", 19.99)]
# Converts the list to a dictionary for easy accessing
hotel_index = dict(hotel_list)

# Defines hotel_cost and returns the total hotel cost
def hotel_cost(city_flight, num_nights):
    hotel_output = hotel_index[city_flight] * num_nights
    return hotel_output

# Defines plane_cost and returns the plane cost
def plane_cost(city_flight):
    if city_flight == "coventry":
        plane_output = 49.99
    elif city_flight == "vilnius":
        plane_output = 99.99
    elif city_flight == "semnan":
        plane_output = 149.99
    else:
        plane_output = 199.99
    return plane_output

# Defines car_rental and returns the total car rental cost
def car_rental(city_flight, rental_days):
    if city_flight == "coventry":
        rental_rate = 24.99
    elif city_flight == "vilnius":
        rental_rate = 19.99
    elif city_flight == "semnan":
        rental_rate = 14.99
    else:
        rental_rate = 9.99
    rental_output = rental_rate * rental_days
    return rental_output

# Defines car_rate and returns the daily car rate
def car_rate(city_flight):
    if city_flight == "coventry":
        rental_rate = 24.99
    elif city_flight == "vilnius":
        rental_rate = 19.99
    elif city_flight == "semnan":
        rental_rate = 14.99
    else:
        rental_rate = 9.99
    return rental_rate

# Defines holiday_cost and returns the total holiday cost
def holiday_cost(hotel_output, plane_output, rental_output):
    holiday_output = hotel_output + plane_output + rental_output
    return holiday_output
