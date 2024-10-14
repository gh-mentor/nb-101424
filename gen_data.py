"""
Create a Python 3.14 function that produces a set of data points (x, y), where x is in the range [1, 20] and y is a random decimal in the range [1000, 5000]. The y value shoud be 2 decimal places of precision. I would like to use NumPy to generate the data points. 
"""

# Importing the required libraries
import random
import numpy as np

# Function to generate the data points
def gen_data(n):
    x = np.arange(1, n+1)
    y = np.round(np.random.uniform(1000, 5000, n), 2)
    return x, y

