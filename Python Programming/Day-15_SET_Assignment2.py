"2. Write a Python program to Return a set of elements present in Set A or B, but not both."

# Define the sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Compute the symmetric difference
result = set1 ^ set2  # This is equivalent to set1.symmetric_difference(set2)

# Print the result
print(result)

#output:
{20, 70, 10, 60}


