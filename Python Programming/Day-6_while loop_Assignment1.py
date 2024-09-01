"1.Write a python program to check whether a number is palindrome or not? "

def is_palindrome(number):
    # Convert the number to a string
    num_str = str(number)
    
    # Compare the string with its reverse
    return num_str == num_str[::-1]

# Example usage
if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        if is_palindrome(number):
            print(f"{number} is a palindrome.")
        else:
            print(f"{number} is not a palindrome.")
    except ValueError:
        print("Please enter a valid integer.")

