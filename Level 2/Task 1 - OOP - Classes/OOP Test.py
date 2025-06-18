class Email:

    classification = "email"

    def __init__(self, subject, sender, date):
        self.subject = subject
        self.sender = sender
        self.date = date

email1 = Email("Subject", "Ethan", "Today")

inbox = [email1]



print (inbox[0].sender)
