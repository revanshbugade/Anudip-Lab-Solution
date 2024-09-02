" 2. Write a Python program to remove a newline in Python"
""" String = "\nBest \nDeeptech \nPython \nTraining\n" """

# Define the input string
string = "\nBest \nDeeptech \nPython \nTraining\n"

# Remove newline characters by replacing them with a space
cleaned_string = string.replace('\n', ' ').strip()

print(f"Original string:\n{string}")
print(f"String after removing newlines:\n{cleaned_string}")


#output
    Original string:
    Best 
    Deeptech 
    Python 
    Training

    String after removing newlines:
    Best Deeptech Python Training
