" 2. Write a Python program to get the largest and smallest number from a list without builtin functions. "

# Define a list of numbers
numbers = [34, 80, 94, 25, 15, 45, 55]

# Initialize the largest and smallest values
# Assuming the list has at least one number
largest = numbers[0]
smallest = numbers[0]

# Iterate through each number in the list
for number in numbers:
    # Update the largest value if the current number is greater
    if number > largest:
        largest = number
    # Update the smallest value if the current number is smaller
    if number < smallest:
        smallest = number

# Print the results
print("The largest number in the list is:", largest)
print("The smallest number in the list is:", smallest)
