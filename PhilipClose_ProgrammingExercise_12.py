# This program is designed to load student exam grades from a CSV file,
# calculate statistics, and determine pass/fail counts for each exam and overall
# performance using NumPy.

# Import numpy for numerical computations. May need to be installed on computer if not already.
import numpy as np

# Define function to load exam data from a CSV file.
def load_data(filename):

    # Load only the exam columns (skipping names) from the CSV, skipping header row.
    data = np.genfromtxt(filename, delimiter=",", skip_header=1, usecols=(2, 3, 4))
    return data

# Define function to print statistics for each exam and overall.
def print_stats(data):

    # Get number of exams.
    number_of_exams = data.shape[1]

    # Loop through each exam and calculate statistics.
    for i in range(number_of_exams):
        exam = data[:, i]
        print(f"\nStatistics for Exam {i + 1}:")
        print(f"  The mean is: {np.mean(exam):.2f}%")
        print(f"  The median is: {np.median(exam):.2f}%")
        print(f"  The standard deviation is: {np.std(exam):.2f}%")
        print(f"  The minimum is: {np.min(exam)}%")
        print(f"  The maximum is: {np.max(exam)}%")

    # Flatten the 2D array into 1D to calculate overall statistics
    all_grades = data.flatten()
    print("\nOverall Statistics of all Exams:")
    print(f"  The mean is: {np.mean(all_grades):.2f}%")
    print(f"  The median is: {np.median(all_grades):.2f}%")
    print(f"  The standard deviation is: {np.std(all_grades):.2f}%")
    print(f"  The minimum is: {np.min(all_grades)}%")
    print(f"  The maximum is: {np.max(all_grades)}%")

# Define function to calculate and display pass/fail statistics.
def pass_rate_stats(data, passing_score=60):

    # Get number of exams.
    number_of_exams = data.shape[1]

    # Initialize total pass counter.
    total_passed = 0

    # Calculate total number of grades.
    total_grades = data.size

    print("\nPass/Fail Counts Per Exam (Passing: 60+):")

    # Loop through each exam to count passes and fails.
    for i in range(number_of_exams):
        passed = np.sum(data[:, i] >= passing_score)
        failed = data.shape[0] - passed
        total_passed += passed
        print(f"  Exam {i + 1}: Passed = {passed}, Failed = {failed}")

    # Calculate and print overall pass percentage.
    pass_percentage = (total_passed / total_grades) * 100
    print(f"\nOverall Pass Percentage: {pass_percentage:.2f}%")

# Define main function to control the program.
def main():

    # Set the filename.
    filename = "grades.csv"

    # Load the exam data from the file.
    data = load_data(filename)

    # Print the first few rows to understand the structure.
    print("First few rows of exam data:")
    print(data[:10])  # Display first 10 rows.

    # Print statistics for each exam and overall.
    print_stats(data)

    # Print pass/fail stats.
    pass_rate_stats(data)

#Call main function.
main()