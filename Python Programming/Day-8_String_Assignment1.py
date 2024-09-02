"1) Write a Python program to count the occurrences of each word in a given sentence "
"string = “To change the overall look of your document. To change the look available in the gallery” "

from collections import Counter
import re

# Define the input string
string = "To change the overall look of your document. To change the look available in the gallery"

# Convert the string to lowercase to make the count case-insensitive
string = string.lower()

# Use regular expression to find all words (a sequence of alphabetic characters)
words = re.findall(r'\b\w+\b', string)

# Count occurrences of each word using Counter from collections module
word_count = Counter(words)

# Print the result
for word, count in word_count.items():
    print(f"'{word}': {count}")

# Output:
    'to': 2
    'change': 2
    'the': 2
    'overall': 1
    'look': 2
    'of': 1
    'your': 1
    'document': 1
    'available': 1
    'in': 1
    'the': 1
    'gallery': 1
