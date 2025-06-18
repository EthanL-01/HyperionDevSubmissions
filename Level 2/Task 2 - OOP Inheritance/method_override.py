class Adult():
    """Defines the default Adult class blueprint.
    """

    def __init__(self, name, age, eye_colour, hair_colour):
        self.name = name
        self.age = age
        self.eye_colour = eye_colour
        self.hair_colour = hair_colour

    def can_drive(self):
        """Method to print that the object is old enough to drive.
        """

        print(f"\nName: {self.name}"
              f"\nAge: {self.age}"
              f"\nEye Colour: {self.eye_colour}"
              f"\nHair Colour: {self.hair_colour}"
            f"\nResult: {self.name} is old enough to drive.")

class Child(Adult):
    """Defines a subclass of the Adult parent object, used to override 
        the parent class when the object is below the minimum driving age.
    """

    def can_drive(self):
        """Override method to print that the object is too young to drive.
        """
        print(f"\nName: {self.name}"
              f"\nAge: {self.age}"
              f"\nEye Colour: {self.eye_colour}"
              f"\nHair: Colour: {self.hair_colour}"
            f"\nResult: {self.name} is too young to drive.")

# Sets a minimum driving age for added code robustness
min_driving_age = 18

# Collects input for name
name = input("\nInput name: ")

# Input validation for collecting the age variable
while True:
    try:
        age = int(input("Input age: "))
        break
    except ValueError:
        print("Please enter a valid number for age.\n")

# Collects inputs for eye and hair colours
eye_colour = input("Input eye colour: ")
hair_colour = input("Input hair colour: ")

# Declares a new object as either Adult or Child based on the age variable
if age <= min_driving_age:
    person1 = Child(name, age, eye_colour, hair_colour)
    # Executes the overrided can_drive() method
    person1.can_drive()
else:
    person1 = Adult(name, age, eye_colour, hair_colour)
    # Executes the original can-drive() method
    person1.can_drive()
