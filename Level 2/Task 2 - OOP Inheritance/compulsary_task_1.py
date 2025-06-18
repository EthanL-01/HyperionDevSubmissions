class Course:
    """Defines the default Course class blueprint.
    """
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"
    head_office = "Cape Town"

    def contact_details(self):
        """Method to print the contact_website attribute
        """
        print(f"\nPlease contact us by visiting {self.contact_website}\n")

    def print_head_office(self):
        """Method to print the head_office attribute
        """
        print(self.head_office)

# Declares the OOPCourse subclass
class OOPCourse(Course):
    """Defines the subclass of the parent Course class.
    """
    # Defines additional attributes for the child independent of the parent
    def __init__(self, description='OOP Fundamentals',
                 trainer='Mr Anon A. Mouse',
                 course_id='#12345'):
        self.description = description
        self.trainer = trainer
        self.course_id = course_id

    def trainer_details(self):
        """Method to print the description and trainer attributes.
        """
        print(f"Course Description: {self.description}")
        print(f"Course Trainer: {self.trainer}")

    def show_course_id(self):
        """Method to print the course_id attribute
        """
        print(f"\nCourse ID: {self.course_id}")

# Declares an object of the OOPCourse subclass, which is a child of the
# Course parent class with additional attributes inherant to itself
course1 = OOPCourse()

# Executes the methods to print relevant inherant and inherited attributes
course1.show_course_id()
course1.trainer_details()
course1.contact_details()
