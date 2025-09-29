# Write a program asking the user for a list of their monthly expenses.
# When asking the user for their expenses, ask for the type of expense and the amount.
# Use the reduce method to analyze the expenses and display the total expense,
# the highest expense and the lowest expense. Label what the highest and lowest expense is.

# import the reduce function from functools category.
from functools import reduce

# main function.
def main():

    # Create a list to hold monthly expenses.
    expenses = []

    # Ask the user for their expenses. The while True loop is used to make an indefinite loop.
    # Ask the user what the expense type is. If they typed done continue the program.
    # Use a try/except statement to get the cost of the expense type.
    print("When you are done inputting expenses type 'done'.")
    while True:
        expenseType = input("What is the monthly expense type? ")
        if expenseType.lower() == 'done':
            break
        try:
            expenseAmount = float(input(f'What is the monthly expense amount for {expenseType}? '))
        except ValueError:
            print("Please enter a numerical value.")
            continue

        # Append both the expense type and expense amount as a group to the expenses list.
        expenses.append((expenseType, expenseAmount))

    # For total expenses, highest expense, and lowest expense, use lambda function to make
    # the program shorter. Here the reduce function will be used to combine the items in a
    # list into a single value. A lambda function is used to shorter the program.
    totalExpenses = reduce(lambda acc, x: acc + x[1], expenses, 0)
    highestExpense = reduce(lambda acc, x: acc if acc[1] > x[1] else x, expenses)
    lowestExpense = reduce(lambda acc, x: acc if acc[1] < x[1] else x, expenses)

    #Print results.
    print(f'Your total monthly expenses are ${totalExpenses:.2f}.')
    print(f'Your highest monthly expense is {highestExpense[0]} at ${highestExpense[1]:.2f}.')
    print(f'Your lowest monthly expense is {lowestExpense[0]} at ${lowestExpense[1]:.2f}.')

#Call main function.
main()