"3. Write a Python program to reverse words in a string "

"String = “Deeptech Python Training” "

# Define the input string
string = "Deeptech Python Training"

# Split the string into a list of words
words = string.split()

# Reverse the list of words
reversed_words = words[::-1]

# Join the reversed list back into a string
reversed_string = ' '.join(reversed_words)

print(f"Original string: '{string}'")
print(f"String after reversing words: '{reversed_string}'")

#output:
    Original string: 'Deeptech Python Training'
    String after reversing words: 'Training Python Deeptech'

        
