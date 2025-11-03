# Create a BankAcct Class that contains at least the following state information:
# name, account number, amount and interest rate. In addition to an __init__ method,
# the class should support methods for adjusting the interest rate, for withdrawing and depositing,
# and for giving a balance. You should also include a method to calculate the interest
# based on the number of days. Use the __str__ method to display balances and interest amounts.

# Create a test function to test the different methods in the BankAcct Class.
class BankAcct:
    def __init__(self, name, account_number, amount, interest_rate):

        # Initialize account details.
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate

    # Define method to adjust the interest rate.
    def adjust_interest_rate(self, new_rate):
        self.interest_rate = new_rate

    # Define method to deposit funds into the account.
    def deposit(self, amount):
        if amount > 0:
            self.amount += amount
        else:
            print("Deposit must be positive.")

    # Define method to withdraw funds from the account.
    def withdraw(self, amount):
        if 0 < amount <= self.amount:
            self.amount -= amount
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    # Define method to check account balance.
    def get_balance(self):
        return self.amount

    # Define method to calculate interest earned over a given number of days.
    def calculate_interest(self, days):
        return self.amount * (self.interest_rate / 100) * (days / 365)

    # Define method to display account details.
    def get_account_details(self):
        return (f"Account Holder: {self.name}\n"
                f"Account Number: {self.account_number}\n"
                f"Balance: ${self.amount:.2f}\n"
                f"Interest Rate: {self.interest_rate}%")

# Define function to test BankAcct class.
def test_bank_account():

    # Create a test account.
    acct = BankAcct("Philip Close", "579384675", 1000000, 3.0)

    # Display initial account details.
    print(acct.get_account_details())

    # Test deposit method.
    acct.deposit(1000)
    print("After deposit:")
    print(acct.get_account_details())

    # Test withdrawal method.
    acct.withdraw(200)
    print("After withdrawal:")
    print(acct.get_account_details())

    # Test interest calculation method.
    interest = acct.calculate_interest(40)
    print(f"Interest earned in last month: ${interest:.2f}")

    # Test interest rate adjustment method.
    acct.adjust_interest_rate(3.5)
    print("After adjusting interest rate:")
    print(acct.get_account_details())

test_bank_account()