"4) Write a Python program that checks if a user-given number is positive, negative, or zero."


# Take user input for the number
number = float(input("Enter a number: "))

# Check if the number is positive, negative, or zero
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")



# output:
    Enter a number: 5
    Positive

    Enter a number: 0
    Zero
