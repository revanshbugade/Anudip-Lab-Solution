"""
1) Create a bar chart to represent monthly expenses in different spending categories and give your conclusion. 
Input: categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation'] 
expenses = [1200, 400, 200, 150, 250]
"""

import matplotlib.pyplot as plt

# Categories and expenses
categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation']
expenses = [1200, 400, 200, 150, 250]

# Create the bar chart
plt.bar(categories, expenses, color=['blue', 'green', 'orange', 'red', 'purple'])
plt.title('Monthly Expenses by Category')
plt.xlabel('Categories')
plt.ylabel('Expenses in Dollars')

# Show the chart
plt.show()
