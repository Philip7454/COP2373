# Create functions to validate phone numbers, social security numbers and zip codes
# using regular expressions. Create a main function to get input from a user and then
# displaying if the phone number, social security number and zip code they entered is valid.
# Be sure to test the functions with various inputs, including valid and invalid examples,
# to ensure the correctness of the regular expressions.

# Import regular expressions.
import re

# Main function.
def main():

    # Get the phone number, ssn, and zip code from the user.
    phoneNumber = input("Type your phone number in the format (123) 456-7890: ")
    ssn = input("Type your SSN in the format 123-45-6789: ")
    zipCode = input("Type your zip code in the format 12345 or 12345-6789: ")

    #Print the results.
    print("Results:")
    print(f"Phone Number Valid? {validate_phone_number(phoneNumber)}")
    print(f"SSN Valid? {validate_ssn(ssn)}")
    print(f"Zip Code Valid? {validate_zip_code(zipCode)}")

# Validate the phone number by checking
# if the user's format matches the program's.
def validate_phone_number(phoneNumber):
    format = r"^\(\d{3}\) \d{3}-\d{4}$"
    return bool(re.match(format, phoneNumber))

# Validate the ssn by checking
# if the user's format matches the program's.
def validate_ssn(ssn):
    format = r"^\d{3}-\d{2}-\d{4}$"
    return bool(re.match(format, ssn))

# Validate the zip code by checking
# if the user's format matches the program's.
def validate_zip_code(zipCode):
    format = r"^\d{5}(-\d{4})?$"
    return bool(re.match(format, zipCode))

#Call main function.
main()