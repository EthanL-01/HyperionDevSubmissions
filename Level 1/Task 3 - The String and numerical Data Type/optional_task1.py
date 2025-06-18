''''
Pseudocode:

Import the math module

Define variables for each side of the triangle
	side_a
	side_b
	side_c
Request input for each and cast to a float

Define the semi perimeter as "semi_peri"
	Calculate the sum of each given side and divide by two, then store this
	in semi_peri
	
Print semi_peri 

Define a variable called "area"
	Apply Heron's formula to calculate the area of the triangle
	Multiply the semi_peri by (semi_peri minus side_a), do the same for 
	side_b and side_c, then find the square root of this output and store
	this in area

Print area using an f-string and limit the output to two decimal points'
'''
# Allows us to use math.sqrt() later to find the square root
import math

# Prompt the user to input values for each side of the triangle
side_a = float(input("Input Side A: "))
side_b = float(input("Input Side B: "))
side_c = float(input("Input Side C: "))

# Stores the semi perimeter of the triangle
semi_peri = ((side_a + side_b + side_c) / 2 )

# Prints the semi perimeter for debugging
print("Semi Perimeter: ", semi_peri)

# Calculates the area of the triangle
area = math.sqrt(semi_peri * (semi_peri - side_a) * 
                             (semi_peri - side_b) *
                             (semi_peri - side_c))

# Prints the area of the triangle and limits the ouput to two decimal points
print(f"Area: {area:.2f}")

# I discovered this while reading a relevant thread on python-forum.io and 
# will need to experiment with it further when working with floats
# Thread: https://python-forum.io/thread-30423.html