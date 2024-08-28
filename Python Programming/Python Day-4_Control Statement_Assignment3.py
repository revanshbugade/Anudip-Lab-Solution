" 3)   Write a Python program that determines if a given year is a leap year or not."


# Take user input for year
year = int(input("Enter a year: "))

# Check if the year is a leap year
if (year % 4 == 0):
    print("Leap year")
else:
    print("Not a leap year")

# output:
    Enter a year: 2024
    Leap year

    Enter a year: 2021
    Not a leap year
