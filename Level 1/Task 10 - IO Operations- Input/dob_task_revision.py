'''
Pseudocode:

Declare list variables for names and dates

Open DOB.txt for reading

Initialize a for loop which executes each line of DOB.txt

    Declare a variable called parts to store each split line into sections for
    reconstruction, making it a list

    Declare variables for name and dob, and join their respective sections
    from the parts list to contruct new strings

    Append each reconstructed string to their respective lists

    Declare variables for names_string and dob_string to recompile the names
    and dates lists into strings for printing

Print names_string and dob_string

Close DOB.txt
'''

# Declares list variables for names and dates
names = []
dates = []

# Opens DOB.txt
with open("DOB.txt", "r") as f:
## Debug: I had trouble with this, as VSCode couldnt find DOB.txt
##        until I opened the folder itself with VSCode, assumedly
##        it was looking in my HyperionDev parent folder rather than
##        in my Task 10 folder

##        I would appreciate feedback on how to remedy this in my code
##        to avoid the need for esoteric workarounds, but honestly as
##        a Star Citizen backer this is pretty par for the course

##        A comment from user ehmatthes helped me understand how to
##        make this work: https://tinyurl.com/EthanLeavold2

# Initializes a for loop which executes for every line of DOB.txt
for line in f:
    # Declares a variable called parts by splitting each line into words
    parts = line.split(" ")

    # Declares variables for name and date of birth and constructs strings
    # for each from their respective parts contained in the parts list
    name = " ".join(parts[0:2])
    dob = " ".join(parts[2:])

    # Appends each reconstructed string to their respective lists
    names.append(name)
    dates.append(dob)

# Declares variables to convert the names and dates lists to strings
names_string = "\n".join(names)
dob_string = "".join(dates)

# Prints the strings
print("Names:")
print(names_string)
print("\nDates of Birth:")
print(dob_string)

# Closes DOB.txt
