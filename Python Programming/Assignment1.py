"""
Lab1: Write a python program using pandas Interpolation to fill in missing values in the data frame.
Input: df = pd.DataFrame({"Math":[12, 4, 7, None, 2], "English":[4, 3, 57, 3, None], "Hindi":[20, 16, None, 3, 8], "Science":[14, 3, None, None, 6]})"""
Solution:-
import numpy as pd
import pandas as pd
from scipy.io import savemat, loadmat

# Create the DataFrame with missing values
data = pd.DataFrame({
    "Math": [12, 4, 7, None, 2],
    "English": [4, 3, 57, 3, None],
    "Hindi": [20, 16, None, 3, 8],
    "Science": [14, 3, None, None, 6]
})

df = pd.DataFrame(data)
df.interpolate(method = 'linear',inplace =True)
#save DataFrame to Matplolib File
savemat('dataframe.mat',{'df':df})

#Load DataFrame from MATLAB file
loaded_data = loadmat ('dataframe.mat')

#Display the original and Loadede DataFrame
print("Original DataFrame")
print(df)
print("\nLoaded DataFRame:")
print(loaded_data)

#OUTPUT:-
Original DataFrame
   Math  English  Hindi  Science
0  12.0      4.0   20.0     14.0
1   4.0      3.0   16.0      3.0
2   7.0     57.0    9.5      4.0
3   4.5      3.0    3.0      5.0
4   2.0      3.0    8.0      6.0

Loaded DataFRame:
{'__header__': b'MATLAB 5.0 MAT-file Platform: nt, Created on: Mon Oct 21 20:09:55 2024', '__version__': '1.0', '__globals__': [], 'df': array([[12. ,  4. , 20. , 14. ],
       [ 4. ,  3. , 16. ,  3. ],
       [ 7. , 57. ,  9.5,  4. ],
       [ 4.5,  3. ,  3. ,  5. ],
       [ 2. ,  3. ,  8. ,  6. ]])}
