# Student Management System

import json

FILE_NAME = "students.json"


def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_students():
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def add_student():
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    course = input("Enter Course: ")

    students[roll_no] = {
        "name": name,
        "course": course
    }

    save_students()
    print("Student added successfully!")


def view_students():
    if not students:
        print("No students found.")
        return

    print("\n--- Student List ---")

    for roll_no, details in students.items():
        print(f"Roll No: {roll_no}")
        print(f"Name: {details['name']}")
        print(f"Course: {details['course']}")
        print("-" * 30)


def search_student():
    roll_no = input("Enter Roll Number to search: ")

    if roll_no in students:
        print("\nStudent Found!")
        print("Roll No:", roll_no)
        print("Name:", students[roll_no]["name"])
        print("Course:", students[roll_no]["course"])
    else:
        print("Student not found.")


def update_student():
    roll_no = input("Enter Roll Number to update: ")

    if roll_no in students:
        print("\nCurrent Details:")
        print("Name:", students[roll_no]["name"])
        print("Course:", students[roll_no]["course"])

        name = input("Enter New Name: ")
        course = input("Enter New Course: ")

        students[roll_no]["name"] = name
        students[roll_no]["course"] = course

        save_students()
        print("Student updated successfully!")
    else:
        print("Student not found.")


def delete_student():
    roll_no = input("Enter Roll Number to delete: ")

    if roll_no in students:
        del students[roll_no]
        save_students()
        print("Student deleted successfully!")
    else:
        print("Student not found.")


students = load_students()


while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Thank you for using Student Management System!")
        break
    else:
        print("Invalid choice. Please try again.")
