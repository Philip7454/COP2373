# An instructor teaches a class in which each student takes three exams.
# The instructor would like to store this information in a file named grades.csv for later use.
# Create a program that allows an instructor to input how many students they want to enter.
# Then enter each student’s first name and last name as strings and the student’s
# three exam grades as integers. Use the csv module to write each record into the grades.csv
# file and have a header of First Name, Last Name, Exam 1, Exam 2 and Exam3.
# Each student should be a record in the grades.csv file.

# Import csv to be able to edit the grades file.
import csv

# The record_grades function allows the teacher/professor edit students' grades.
def record_grades():

    # Make a variable for the file name (technically optional if only using one file).
    filename = "grades.csv"

    # Ask the user how many students' grades they are putting in.
    studentAmount = int(input("How many students are you grading? 1"))

    # Open the file and put in the header and new grades.
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])
        for x in range(studentAmount):
            firstName = input("Student's first name: ")
            lastName = input("Student's last name: ")
            exam1 = int(input("First exam grade: "))
            exam2 = int(input("Second exam grade: "))
            exam3 = int(input("Third exam grade: "))
            writer.writerow([firstName, lastName, exam1, exam2, exam3])
            print(f"\nGrades updated.")

# The see_grades function allows the teacher/professor to see the grades
# that he or she has already put in.
def see_grades():
    filename = "grades.csv"

    # Use a try/except loop to try to open the file if it exists.
    try:

        # Open the file and display the contents in tabular form.
        with open(filename, mode="r") as file:
            reader = csv.reader(file)
            content = list(reader)
            if len(content) == 0:
                print(f"There is nothing in the file.\nPlease enter student grades first.")
                return
            print("\n{:<15} {:<15} {:<10} {:<10} {:<10}".format(*content[0]))
            print("-" * 60)
            for row in content[1:]:
                print("{:<15} {:<15} {:<10} {:<10} {:<10}".format(*row))
            print("")
    except FileNotFoundError:
        print("No file called grades.csv exists. Please enter student grades first.")

# The main function holds the selection menu.
def main():

    # The user can make a selection during the program to either add grades,
    # see grades, or exit the program.
    print(f"Welcome to the teacher gradebook.\nPlease type a number to get started:")
    while True:
        print("1 = Edit student grades")
        print("2 = Read student grades")
        print("3 = End the program")
        choice = int(input(""))
        if choice == 1:
            record_grades()
        elif choice == 2:
            see_grades()
        elif choice == 3:
            print("Process complete")
            break
        else:
            print("Please enter a number 1-3.")

#Call main function.
main()