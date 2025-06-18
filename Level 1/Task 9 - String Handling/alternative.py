'''
Pseudocode:

Declare a variable containing a string
Declare a variable that converts the string to a list of it's characters

Write a for loop which will execute every other character in the list
    Convert each of these entries in the for loop to uppercase

Join each character in the list back into a string and print

---

Declare a variable that splits the string into a list of words

Write a for loop identical to the first but refers to string_split


'''
# Declares a string variable and another that converts the string to a list
string = "my spoon is too big"
string_list = list(string)

# Executes for every other character in the list and changes them to uppercase
for i in range (0,len(string),2):
    string_list[i] = string_list[i].upper()

# Recompiles the list into a string
string_list = "".join(string_list)

# Prints the updated and recompiled string
print(string_list)

# I used a comment from a deleted user halfway down the thread to help me
# understand how to complete the task: https://tinyurl.com/EthanLeavold

# Declares a variable that splits each word in the original string into a
# list of it's words
string_split = string.split()

# Executes for every other word in the list and changes them to uppercase
for i in range (0,len(string_split),2):
    string_split[i] = string_split[i].upper()

# Recompiles the list into a string
string_split = " ".join(string_split)

# Prints the updated and recompiled string
print(string_split)

# I've taken what I learned from the URL above and applied it to the second
# half of the assignment
