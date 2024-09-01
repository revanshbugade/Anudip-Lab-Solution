"2. Write a python program finding the factorial of a given number using a while loop"

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result

# Example usage
if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        print(f"The factorial of {number} is {factorial(number)}.")
    except ValueError:
        print("Please enter a valid integer.")


