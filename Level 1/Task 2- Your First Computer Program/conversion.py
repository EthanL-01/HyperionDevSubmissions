'''
Pseudocode:

Declare the following variables
    num1 = 99.23
    num2 = 23
    num3 = 150
    string1 = “100”

Convert each one to a new data type
    num1 as an integer
    num2 as an float
    num3 as an string
    string1 as an integer

Print each variable once they have been converted

'''
#define each variable and convert each to their new data type
num1 = int(99.23)
num2 = float(23)
num3 = str(150)
string1 = int("100")

# I've included this redundant block of code to demonstrate how I've made my code more succint
'''
num1 = int(num1)
num2 = float(num2)
num3 = str(num3)
string1 = int(string1)
'''

#outputs each variable as their converted data type
print(num1)
print(num2)
print(num3)
print(string1)