"2. Python program to check if a given number is an Armstrong number"


def is_armstrong_number(number):
    # Convert the number to a string to easily iterate over digits
    num_str = str(number)
    # Get the number of digits
    num_digits = len(num_str)
    
    # Compute the sum of each digit raised to the power of num_digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the sum of the powers is equal to the original number
    return sum_of_powers == number

# Input from the user
try:
    input_number = int(input("Enter a number to check if it is an Armstrong number: "))
    
    # Check and output the result
    if is_armstrong_number(input_number):
        print(f"{input_number} is an Armstrong number.")
    else:
        print(f"{input_number} is not an Armstrong number.")
except ValueError:
    print("Please enter a valid integer.")


  # output:
    Enter a number to check if it is an Armstrong number: 23
    23 is not an Armstrong number.
