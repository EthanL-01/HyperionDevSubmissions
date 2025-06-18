import sqlite3

# Defines the Student class
class Student:
    def __init__(self, studentid, name, grade):
        self.studentid = studentid
        self.name = name
        self.grade = grade

# Defines each student as a Student object with relevant data
student1 = Student(55, 'Carl Davis', 61)
student2 = Student(66, 'Dennis Fredrickson', 88)
student3 = Student(77, 'Jane Richards', 78)
student4 = Student(12, 'Peyton Sawyer', 45)
student5 = Student(2, 'Lucas Brooke', 99)

# Stores each Student object for inserting into the table
student_info = [student1, student2, student3, student4, student5]

try:
    # Declares the .db file for writing to
    db = sqlite3.connect('task6database.db')
    cursor = db.cursor()

    # DEBUG: Used to remove the table for repeat testing
    # DEBUG: Comment this block out if it's causing issues
    cursor.execute('''DROP TABLE python_programming''')
    db.commit()

    # Creates the table
    cursor.execute('''
                   CREATE TABLE python_programming(
                   id INTEGER, 
                   name STRING, 
                   grade INTEGER)
                   ''')
    db.commit()

    # Inserts each Student object stored into the table
    cursor = db.cursor()
    for Student in student_info:
        cursor.execute('''
                        INSERT INTO python_programming(id, name, grade)
                        VALUES(?,?,?)''', (Student.studentid, Student.name,
                                           Student.grade))
        print(f"Student ID: {Student.studentid} - {Student.name} inserted\n")

    # Selects and outputs a list of students
    cursor.execute('''
                   SELECT * 
                   FROM python_programming
                   ''')
    student_output = cursor.fetchall()
    print(f"Students:\n{student_output}\n")

    # Selects and outputs each student with a grade between 60 and 80
    cursor.execute('''
                   SELECT name, grade 
                   FROM python_programming 
                   WHERE grade 
                   BETWEEN 60 AND 80
                   ''')
    student_output = cursor.fetchall()
    print(f"Students with grades between 60 and 80:\n{student_output}\n")

    # Updates "Carl Davis" grade to 65
    cursor.execute('''
                   UPDATE python_programming 
                   SET grade = 65 
                   WHERE id = 55
                   ''')
    db.commit()

    # Selects "Carl Davis" and outputs a string saying their grade
    # has been updated
    cursor.execute('''
                   SELECT name 
                   FROM python_programming 
                   WHERE id = 55
                   ''')
    student_output = cursor.fetchone()
    print(f"Student \"{student_output[0]}\" has had their grade "
          "updated to 65\n")

    # Deletes "Dennis Fredrickson" record from the table
    cursor.execute('''
                   DELETE FROM python_programming 
                   WHERE id = 66
                   ''')
    db.commit()

    # Updates the grade of each student with an id >= to 80
    cursor.execute('''
                   UPDATE python_programming 
                   SET grade = 80 
                   WHERE id >= 55
                   ''')
    db.commit()

    # Selects each student with an id >= 55 and outputs a string informing
    # their grade has been updated
    cursor.execute('''
                   SELECT name 
                   FROM python_programming 
                   WHERE id >= 55
                   ''')
    student_output = cursor.fetchall()
    print(f"Students {', and '.join([student[0]
            for student in student_output])} "
           "have had their grades updated to 80\n")

    # Selects and outputs a list of students
    cursor.execute('''SELECT * FROM python_programming''')
    student_output = cursor.fetchall()
    print(f"Students:\n{student_output}\n")

except sqlite3.Error as e:
    db.rollback()
    print("An error has occured")
    raise e

finally:
    db.commit()
    db.close()
