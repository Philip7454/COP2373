# Write a program that will allow me to enter a paragraph,
# including sentences which begin with numbers.
# Display each individual sentence and the count of sentences in the paragraph.

# Import regular functions.
import re

# Main function.
def main():

    #Initialize variables.
    paragraph = input("Input the paragraph: ")

    # Call the get_sentences function.
    sentences = get_sentences(paragraph)

    # Print results.
    print(f"There are {len(sentences)} sentences in this paragraph.")
    print(f"They are:")

    # Use a for loop to enumerate the sentences in the paragraph.
    for n, sentence in enumerate(sentences, start=1):
        print(f"{n}. {sentence}")

# get_sentences function splits the paragraph into sentences.
def get_sentences(paragraph):

    # Input the pattern to find sentences.
    sentenceFormat = r'(?<=[.!?])(?=\s*[A-Z0-9])'

    # Split the paragraph into sentences and return result.
    sentences = re.split(sentenceFormat, paragraph)
    return [s.strip() for s in sentences if s.strip()]

#Call main function.
main()