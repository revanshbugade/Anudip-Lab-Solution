"""
1: Write a Pandas program to split the following data frame into groups based on Class and count the number of students in that particular class.
Also generate a bar chart based on the result and explain the conclusion."""

import pandas as pd
import matplotlib.pyplot as plt

# Create the DataFrame
student_data = pd.DataFrame({
    'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'],
    'class': ['V', 'VI', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']
})

# Group by class and count the number of students
class_counts = student_data['class'].value_counts()

# Print the counts
print(class_counts)

# Generate a bar chart
class_counts.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Number of Students in Each Class')
plt.xlabel('Class')
plt.ylabel('Number of Students')
plt.xticks(rotation=0)
plt.show()

