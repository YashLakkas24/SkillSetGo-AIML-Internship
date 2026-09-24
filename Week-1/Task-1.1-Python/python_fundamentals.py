# ============================================================
# Task 1.1 - Python Fundamentals
# Skill Set Go EduTech AI/ML Internship
# ============================================================


# ------------------------------------------------------------
# 1. Variables and Data Types
# ------------------------------------------------------------

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# branch = input("Enter your branch: ")
# cgpa = float(input("Enter your CGPA: "))

# print("\nStudent Information")
# print("Name:", name)
# print("Age:", age)
# print("Branch:", branch)
# print("CGPA:", cgpa)


# # ------------------------------------------------------------
# # 2. Lists
# # ------------------------------------------------------------

# marks = list(map(int, input("\nEnter 5 marks separated by spaces: ").split()))

# print("\nMarks:", marks)
# print("Maximum:", max(marks))
# print("Minimum:", min(marks))
# print("Average:", sum(marks) / len(marks))
# print("Sorted:", sorted(marks))


# # ------------------------------------------------------------
# # 3. Dictionaries
# # ------------------------------------------------------------

# student = {}

# student["name"] = input("\nEnter student name: ")
# student["age"] = int(input("Enter student age: "))
# student["branch"] = input("Enter branch: ")
# student["cgpa"] = float(input("Enter CGPA: "))
# student["skills"] = input("Enter skills separated by commas: ").split(",")

# # Add a new key
# student["college"] = "Thakur College of Engineering & Technology"

# # Update an existing value
# student["cgpa"] = float(input("Enter updated CGPA: "))

# print("\nStudent Dictionary")

# for key, value in student.items():
#     print(key, "->", value)


# # ------------------------------------------------------------
# # 4. Functions
# # ------------------------------------------------------------


# def calculate_average(marks):
#     """Calculate and return the average of a list of marks."""
#     return sum(marks) / len(marks)


# average = calculate_average(marks)

# print("\nAverage using function:", average)

# if average >= 40:
#     print("Status: Pass")
# else:
#     print("Status: Fail")


# try:
#     numerator = int(input("Enter numerator: "))
#     denominator = int(input("Enter denominator: "))

#     print("Result:", numerator / denominator)

# except ValueError:
#     print("Error: Please enter valid numbers.")

# except ZeroDivisionError:
#     print("Error: Cannot divide by zero.")


# # ------------------------------------------------------------
# # 5. File Handling
# # ------------------------------------------------------------

# with open("student.txt", "w") as file:
#     name = input("Enter your name: ")
#     age = int(input("Enter your age: "))
#     branch = input("Enter your branch: ")
#     cgpa = float(input("Enter your CGPA: "))

#     file.write("Name: " + name + "\n")
#     file.write("Age: " + str(age) + "\n")
#     file.write("Branch: " + branch + "\n")
#     file.write("CGPA: " + str(cgpa) + "\n")


# with open("student.txt", "r") as file:
#     print("\nStudent Information from File:")
#     print(file.read())

# ------------------------------------------------------------
# 6. Object-Oriented Programming
# ------------------------------------------------------------


class Student:
    def __init__(self, name, branch):
        self.name = name
        self.branch = branch

    def display_info(self):
        print(f"{self.name} - {self.branch}")


class EngineeringStudent(Student):
    def __init__(self, name, branch, cgpa):
        super().__init__(name, branch)
        self.cgpa = cgpa

    def display_info(self):
        print(f"{self.name} - {self.branch} - CGPA: {self.cgpa}")


student = EngineeringStudent("Rahul", "AI/DS", 8.5)
student.display_info()
