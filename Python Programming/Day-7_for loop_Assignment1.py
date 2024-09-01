"1.Python program to check if the given string is a palindrome "



def is_palindrome(s):
    # Remove any non-alphanumeric characters and convert to lowercase
    cleaned_string = ''.join(c.lower() for c in s if c.isalnum())
    
    # Check if the cleaned string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]

# Input from the user
input_string = input("Enter a string to check if it is a palindrome: ")

# Check and output the result
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


# output
    Enter a string to check if it is a palindrome: 121
    The string is a palindrome.
