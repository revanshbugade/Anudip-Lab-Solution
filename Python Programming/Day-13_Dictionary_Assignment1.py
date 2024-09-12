"1. Write a Python program and calculate the mean of the below dictionary."

" test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4} "
 
# Define the dictionary
test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}

# Extract the values from the dictionary
values = test_dict.values()

# Calculate the sum of the values
total_sum = sum(values)

# Calculate the number of values
num_values = len(values)

# Calculate the mean
mean = total_sum / num_values

# Print the result
print("Output:", mean)

#output:
Output: 6.2
