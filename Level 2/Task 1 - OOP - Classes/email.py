from datetime import datetime

### --- OOP Email Simulator --- ###

# Declares the "Email" class
class Email():
    """This is the blueprint for an email object.
    """
    classification = "email"
    has_been_read = False
    is_spam = False

    # Initializes the constructor for the class
    def __init__(self, email_address, subject_line, email_contents, date):
        """Initializes the class constructor and unique email attributes.
        """
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_contents = email_contents
        self.date = date

    # Function for marking an email as read
    def mark_as_read(self):
        """Handles marking an email as read.
        """
        self.has_been_read = True

# --- Lists --- #

# Initializes an empty list for storing emails
inbox = []

# --- Functions --- #

# Function for getting today's date, non-essential more for fun
def get_date():
    """Handles getting today's date.
    """
    date = datetime.today().strftime("%d %B %Y")
    return date

# Function for adding example emails to "inbox"
def populate_inbox():
    """Handles adding test emails to the inbox list.
    """
    example1 = Email("ethan@aol.com", "Due Date!", "Urgent, reply ASAP!", get_date())
    example2 = Email("rhys@aol.com", "What's up?", "The guys and I are going to the "
        "movies, wanna come?", get_date())
    example3 = Email("chris@aol.com", "New Recipes", "We're designing a new menu and "
        "we'd love to get your feedback.", get_date())
    inbox.append(example1)
    inbox.append(example2)
    inbox.append(example3)

# Function for listing unread emails
def list_unread_emails(inbox):
    """Handles displaying emails in index order.
    """
    unread_found = False
    print()
    for counter, email in enumerate(inbox):
        if not email.has_been_read and not email.is_spam:
            print(counter, email.subject_line)
            unread_found = True
    if not unread_found:
        print("No unread emails.")

# Function for listing all non-spam emails, unread or not
def list_emails(inbox):
    """Handles displaying all emails in index order.
    """
    print()
    for counter, email in enumerate(inbox):
        print(counter, email.subject_line)

# Function for listing spam emails
def list_spam_emails(inbox):
    """Handles displaying spam emails in index order.
    """
    spam_found = False
    print()
    for counter, email in enumerate(inbox):
        if email.is_spam == True:
            print(counter, email.subject_line)
            spam_found = True
    if not spam_found:
        print("No spam emails.")

def mark_as_spam(inbox):
    """Handles marking an email as spam.
    """
    try:
        index = int(input("\nEmail index: "))

        if index < 0:
            print("Invalid Negative Email Index. Please try again.")

        inbox[index].is_spam = True
        print("\nEmail has been marked as spam.")
    except ValueError:
        print("\nInvalid input. Please try again.")

def delete_email(inbox):
    """Handles deleting an email from the inbox list.
    """
    try:
        index = int(input("\nEmail index: "))

        if index < 0:
            print("Invalid Negative Email Index. Please try again.")

        inbox.pop(index)
        print("\nEmail has been deleted.")
    except ValueError:
        print("\nInvalid input. Please try again.")
    except IndexError:
        print("\nInvalid Email Index. Please try again.")

# Function to read a specific email by inputting it's index number
def read_email(inbox):
    """Allows the user to read an email by inputting it's inbox index number.
    """
    try:
        index = int(input("\nEmail index: "))

        if index < 0:
            print("Invalid Negative Email Index. Please try again.")

        email = inbox[index]
        print(f"\nSender: {email.email_address}")
        print(f"Subject: {email.subject_line}")
        print(f"Contents: {email.email_contents}")
        print(f"Date Sent: {email.date}")
        email.mark_as_read()
        print(f"\n Email has been marked as read.")

    except IndexError:
        print("\nInvalid Email Index. Please try again.")

# --- Email Program --- #

# Populates "inbox" with three example emails
populate_inbox()

menu = True

# Executes and displays menu options until the user exits the program
while menu:
    try:
        user_choice = int(input('''\nWould you like to:
        1. Read an email
        2. View unread emails
        3. View all emails
        4. View spam email
        5. Mark as spam
        6. Delete email
        7. Quit application

        Enter selection: '''))

    except ValueError:
        print("\nOops - incorrect input.")
        continue

    # Allows the user to read an email stored in "inbox"
    if user_choice == 1:
        read_email(inbox)

    # Lists all emails who's attribute "has_been_read" equals False
    elif user_choice == 2:
        list_unread_emails(inbox)

    # Lists all emails, regardless of spam, unread or not
    elif user_choice == 3:
        list_emails(inbox)

    # Lists all emails who's attribute "is_spam" equals True
    elif user_choice == 4:
        list_spam_emails(inbox)

    # Allows the user to mark an email as spam
    elif user_choice ==5:
        mark_as_spam(inbox)

    # Allows the user to delete an email from inbox
    elif user_choice == 6:
        delete_email(inbox)

    # Exits the program by terminating the loop
    elif user_choice == 7:
        print("\nGoodbye!")
        menu = False
