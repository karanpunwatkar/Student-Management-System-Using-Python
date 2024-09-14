import sqlite3

# Connect to SQLite Database (or create it if it doesn't exist)
conn = sqlite3.connect('student_management_system.db')
cursor = conn.cursor()

# Create Table if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    roll_number INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    student_class TEXT NOT NULL,
    email TEXT NOT NULL,
    address TEXT NOT NULL,
    mobile_number TEXT NOT NULL
)
''')

class Student:
    def __init__(self, roll_number, name, age, student_class, email, address, mobile_number):
        self.roll_number = roll_number
        self.name = name
        self.age = age
        self.student_class = student_class
        self.email = email
        self.address = address
        self.mobile_number = mobile_number

class StudentManagementSystem:

    @staticmethod
    def add_student(student):
        cursor.execute('''
        INSERT INTO students (roll_number, name, age, student_class, email, address, mobile_number)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (student.roll_number, student.name, student.age, student.student_class, student.email, student.address, student.mobile_number))
        conn.commit()
        print("Student added successfully.")

    @staticmethod
    def delete_student(roll_number):
        cursor.execute('DELETE FROM students WHERE roll_number = ?', (roll_number,))
        conn.commit()
        print("Student deleted successfully.")

    @staticmethod
    def update_student(roll_number, attribute, new_value):
        query = f"UPDATE students SET {attribute} = ? WHERE roll_number = ?"
        cursor.execute(query, (new_value, roll_number))
        conn.commit()
        print(f"Student's {attribute} updated successfully.")

    @staticmethod
    def display_students():
        cursor.execute('SELECT * FROM students')
        students = cursor.fetchall()

        if len(students) == 0:
            print("No student information available.")
        else:
            for student in students:
                print(f"Roll Number: {student[0]}, Name: {student[1]}, Age: {student[2]}, Class: {student[3]}, Email: {student[4]}, Address: {student[5]}, Mobile: {student[6]}")
                print("-" * 50)

    @staticmethod
    def get_student_by_roll(roll_number):
        cursor.execute('SELECT * FROM students WHERE roll_number = ?', (roll_number,))
        student = cursor.fetchone()
        if student:
            print(f"Roll Number: {student[0]}, Name: {student[1]}, Age: {student[2]}, Class: {student[3]}, Email: {student[4]}, Address: {student[5]}, Mobile: {student[6]}")
        else:
            print("Student not found.")

def main():
    while True:
        print("Welcome to the Student Management System")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Update Student")
        print("4. Display All Students")
        print("5. Get Student By Roll Number")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            roll_number = int(input("Enter Roll Number: "))
            name = input("Enter Name: ").upper()
            age = int(input("Enter Age: "))
            student_class = input("Enter Class: ").upper()
            email = input("Enter Email: ").lower()
            address = input("Enter Address: ").upper()
            mobile_number = input("Enter Mobile Number: ")

            if len(mobile_number) != 10:
                print("Invalid Mobile Number. Must be 10 digits.")
                continue

            student = Student(roll_number, name, age, student_class, email, address, mobile_number)
            StudentManagementSystem.add_student(student)

        elif choice == '2':
            roll_number = int(input("Enter Roll Number of student to delete: "))
            StudentManagementSystem.delete_student(roll_number)

        elif choice == '3':
            roll_number = int(input("Enter Roll Number of student to update: "))
            attribute = input("Enter attribute to update (name, age, student_class, email, address, mobile_number): ").lower()
            new_value = input(f"Enter new value for {attribute}: ").upper()
            StudentManagementSystem.update_student(roll_number, attribute, new_value)

        elif choice == '4':
            StudentManagementSystem.display_students()

        elif choice == '5':
            roll_number = int(input("Enter Roll Number: "))
            StudentManagementSystem.get_student_by_roll(roll_number)

        elif choice == '6':
            print("Exiting system.")
            conn.close()
            break

        else:
            print("Invalid option. Please choose again.")

if __name__ == '__main__':
    main()
