# Suppose you have a dataset containing daily temperature readings for a city, and you want to identify days with extreme temperature conditions. Find days where the temperature either exceeded 35 degrees Celsius (hot day) or dropped below 5 degrees Celsius (cold day). 
# Input: temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2,-4,-12])

import numpy as np

# Array of temperature readings
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2, -4, -12])

# Condition for hot days (temperature > 35 degrees)
hot_days_indices = np.where(temperatures > 35)[0]

# Condition for cold days (temperature < 5 degrees)
cold_days_indices = np.where(temperatures < 5)[0]

# Display hot days with their day indices and temperatures
print("Hot days:")
print("Day   Temperature (°C)")
for i in hot_days_indices:
    print(f"{i+1}     {temperatures[i]:.1f}")

# Display cold days with their day indices and temperatures
print("\nCold days:")
print("Day   Temperature (°C)")
for i in cold_days_indices:
    print(f"{i+1}     {temperatures[i]:.1f}")


# Output:

# Hot days:
# Day   Temperature (°C)
# 3     36.8
# 6     38.7
# 10     37.2

# Cold days:
# Day   Temperature (°C)
# 11     -4.0
# 12     -12.0

