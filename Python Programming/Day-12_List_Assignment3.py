" 3. Write a Python program to find duplicate values from a list and display those. "

# Define a list of numbers
numbers = [10, 20, 10, 30, 40, 20, 50, 30, 60]

# Create an empty dictionary to store occurrences
occurrences = {}

# Iterate through each number in the list
for number in numbers:
    if number in occurrences:
        occurrences[number] += 1
    else:
        occurrences[number] = 1

# Create a list to store duplicate values
duplicates = [number for number, count in occurrences.items() if count > 1]

# Print the duplicate values
print("Duplicate values in the list are:", duplicates)
