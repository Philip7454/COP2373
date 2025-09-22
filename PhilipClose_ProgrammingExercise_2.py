# Spam (or junk email) costs U.S. organizations billions of dollars a year in spam-prevention
# software, equipment, network resources, bandwidth, and lost productivity.
# Research online some of the most common spam email messages and words.
# Create a list of 30 words and phrases commonly found in spam messages.
# Write an application in which the user enters an email message.
# Then your application will scan the message for each of the 30 keywords or phrases.
# For each occurrence of one of these within the message, add a point to the message's "spam score".
# Next, rate the likelihood that the message is spam, based on the number of points received.
# Display the user's spam score, the likelihood message that it is spam,
# and the words/phrases which caused it to be spam.

# Main function
def main():

    # The emailText variable holds the email.
    emailText = input("Enter the suspicious email: ")

    # The spamPhrases variable holds the amount of spam words or phrases counted in the email
    # while the spamFound list holds the specific words or phrases that are counted as spam.
    spamPhrases, spamFound = calculate_spam_words(emailText)

    # The spamScore variable holds the probability of the email being spam.
    spamScore = calculate_spam_score(spamPhrases)

    # Print results.
    print("\n--- Scam Score ---")
    print(f"There are {spamPhrases} instances of spam words or phrases.")
    print(f"The flagged words and/or phrases are: {', '.join(spamFound)}")
    print(f"This email is {spamScore} to be spam.")

# The calculate_spam_words function calculates how many spam words are in the email
# and which words or phrases are triggered.
def calculate_spam_words(email):

    #spamWords holds the 30 words and phrases used to check if the email is spam.
    spamWords = [
        "congratulations", "winner", "free", "urgent", "act now", "limited time",
        "exclusive deal", "important notice", "verify your account", "click here",
        "update required", "security alert", "confirm your password", "suspicious activity",
        "final warning", "immediate action", "unusual login attempt", "attention",
        "access restricted", "you have been selected", "100% free", "risk-free", "no cost",
        "offer expires", "money-back guarantee", "once in a lifetime", "act immediately",
        "claim your prize", "banking information", "wire transfer"
    ]

    # Initialize variables.
    email = email.lower()
    spamAmount = 0
    spamFound = []

    # Used a for loop with an if statement to check the entire email for
    # suspicious words and phrases. When one is found. The spam count goes up
    # and the word or phrase is added to the list.
    for word in spamWords:
        if word in email:
            spamAmount += 1
            spamFound.append(word)

    # Return results to the main function.
    return spamAmount, spamFound

# The calculate_spam_score function determines the probability of the email being spam.
def calculate_spam_score(spamPhrases):

    # Initialize variable.
    possibility = ""

    # Use if else chain to determine the likelihood of the email being scam.
    if spamPhrases == 0:
        possibility = "highly unlikely"
    elif spamPhrases < 3:
        possibility = "not likely"
    elif spamPhrases < 5:
        possibility = "likely"
    else:
        possibility = "highly likely"

    # Return results to the main function.
    return possibility

# Call the main function.
main()