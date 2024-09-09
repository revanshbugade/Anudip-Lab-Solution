"1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero."
def divide_numbers():
    try:
        # Input: take two numbers from the user
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        
        # Perform division
        result = numerator / denominator
        
    except ZeroDivisionError:
        # Handle the case where the denominator is zero
        print("Error: Cannot divide by zero.")
    except ValueError:
        # Handle invalid input (not a number)
        print("Error: Please enter a valid number.")
    else:
        # If no exceptions occurred, print the result
        print(f"The result of {numerator} divided by {denominator} is {result}.")
    finally:
        # This block is executed no matter what
        print("Execution completed.")

# Call the function to run the program
divide_numbers()

#output
Enter the numerator: 8
Enter the denominator: 4
The result of 8.0 divided by 4.0 is 2.0.
Execution completed.
