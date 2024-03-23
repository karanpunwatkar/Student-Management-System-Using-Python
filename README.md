# Student-Management-System-Using-Python
This Python code establishes a Student Management System (SMS) for organizing student data. It enables users to add, delete, update, and display student information through an interactive command-line interface, facilitating efficient administrative tasks.

The code defines a student management system that allows the user to add, delete, update, and display student information. Here's a breakdown of each part of the code:
1. Importing the sys module: This module provides access to some variables used or maintained by the Python interpreter and to functions that interact strongly with the interpreter.
2. Defining global lists to store student information: The code defines several lists to store different pieces of student information, such as name, roll number, address, email, age, and mobile number.
3. Defining the STUDENT_MANAGEMENT_SYSTEM class: This class contains all the methods needed to manage student information.
4. ADD_STUDENT_INFORMATION method: This method prompts the user to enter student information and adds it to the appropriate global lists.
5. DELETE_STUDENT_INFORMATION method: This method prompts the user to enter a roll number and removes the corresponding student information from the global lists.
6. UPDATE_STUDENT_INFORMATION method: This method prompts the user to enter the attribute they want to update and the new value. It then finds the corresponding student information in the global lists and updates it.
7. DISPLAY_STUDENT_INFORMATION method: This method prints out all the student information stored in the global lists.
8. Creating an instance of the STUDENT_MANAGEMENT_SYSTEM class: The code creates an instance of the class so that the methods can be called.
9. The main loop: The code uses a while loop to repeatedly prompt the user to choose an option from a menu.

Overall, the code is a simple implementation of a student management system that uses global variables to store student information. While this approach can work for small programs, it's generally not recommended for larger programs because it can make the code harder to maintain and debug. Instead, it's better to use classes and objects to encapsulate data and behavior.
