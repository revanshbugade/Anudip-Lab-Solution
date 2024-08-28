" 5) Write a Python program that determines the largest of three."


# Take user input for three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Determine the largest of the three numbers
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Print the largest number
print("The largest number is:", largest


# output:
        Enter the first number: 100
        Enter the second number: 20
        Enter the third number: 300
        The largest number is: 300.0
