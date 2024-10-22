"""Lab2: Write a python program using Interpolation to fill in missing values in the data frame. After that store the data frame into a MATLAB file using SciPy IO.Then display the contents from the MATLAB file. 
Input: df = pd.DataFrame({"Math":[12, 4, 7, None, 2], "English":[4, 3, 57, 3, None], "Hindi":[20, 16, None, 3, 8], "Science":[14, 3, None, None, 6]})"""
Solution:-
import pandas as pd
from scipy.io import savemat, loadmat

# Create the DataFrame with missing values
df = pd.DataFrame({
    "Math": [12, 4, 7, None, 2],
    "English": [4, 3, 57, 3, None],
    "Hindi": [20, 16, None, 3, 8],
    "Science": [14, 3, None, None, 6]
})

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Use interpolation to fill missing values
df_interpolated = df.interpolate()

# Display the DataFrame after interpolation
print("\nDataFrame after interpolation:")
print(df_interpolated)

# Save the DataFrame to a MATLAB file
matlab_file_name = 'data.mat'
savemat(matlab_file_name, {'data': df_interpolated})

# Load the contents from the MATLAB file
loaded_data = loadmat(matlab_file_name)

# Extract and display the data
print("\nContents from the MATLAB file:")
print(loaded_data['data'])

#OUTPUT:-
Original DataFrame:
   Math  English  Hindi  Science
0  12.0      4.0   20.0     14.0
1   4.0      3.0   16.0      3.0
2   7.0     57.0    NaN      NaN
3   NaN      3.0    3.0      NaN
4   2.0      NaN    8.0      6.0

DataFrame after interpolation:
   Math  English  Hindi  Science
0  12.0      4.0   20.0     14.0
1   4.0      3.0   16.0      3.0
2   7.0     57.0    9.5      4.0
3   4.5      3.0    3.0      5.0
4   2.0      3.0    8.0      6.0

Contents from the MATLAB file:
[[12.   4.  20.  14. ]
 [ 4.   3.  16.   3. ]
 [ 7.  57.   9.5  4. ]
 [ 4.5  3.   3.   5. ]

