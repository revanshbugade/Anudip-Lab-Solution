"2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer."

def get_integer_input():
    try:
        # Prompt the user for input
        user_input = input("Please enter an integer: ")
        
        # Try to convert the input to an integer
        number = int(user_input)
        
    except ValueError:
        # Raise a ValueError if conversion fails
        print("Error: The input is not a valid integer.")
        raise  # Re-raise the exception to indicate that an error occurred
    else:
        # If no exception occurred, print the valid integer
        print(f"You entered the integer: {number}")
    finally:
        # This block executes no matter what
        print("Execution completed.")

# Call the function to run the program
get_integer_input()


#output
Please enter an integer: 24
You entered the integer: 24
Execution completed.
