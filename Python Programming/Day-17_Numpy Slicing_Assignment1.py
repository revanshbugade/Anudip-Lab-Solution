import numpy as np

# Create arrays
zeros_array = np.zeros(10)
ones_array = np.ones(10)
fives_array = np.full(10, 5)

# Combine the arrays
result_array = np.concatenate((zeros_array, ones_array, fives_array))

print(result_array)
