"""
This app uses Python 3.14, numpy, pandas, matplotlib to generate a set of data points and plot them on a graph.
"""

# Importing the required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
Create a function 'gendatapoints' that generates a set of 100 data points (x, f(x)) and returns them as a pandas data frame.
Arguments:
- 'x_range' is a tuple of two integers representing the range of x values to generate.
Returns:
- A pandas data frame with two columns, 'x' and 'y'.
Details:
- 'x' values are generated randomly between x_range[0] and x_range[1].
- 'y' values are generated as a non-linear function of x with excessive random noise: y = x ^ 1.5  + noise.
- The data frame is sorted by the 'x' values.
- The data frame has 100 rows.
Error Handling:
- Raise a ValueError if x_range is not a tuple of two integers.
- Raise a ValueError if x_range[0] is greater than x_range[1].
Examples:
- gendata((0, 100)) generates a data frame with 'x' values between 0 and 100.
- gendata((-100, 100)) generates a data frame with 'x' values between -100 and 100.
"""

def gendatapoints(x_range):
    if not isinstance(x_range, tuple) or len(x_range) != 2 or not all(isinstance(i, int) for i in x_range):
        raise ValueError("x_range must be a tuple of two integers.")
    if x_range[0] > x_range[1]:
        raise ValueError("x_range[0] must be less than or equal to x_range[1].")
    np.random.seed(0)
    x = np.random.randint(x_range[0], x_range[1], 100)
    noise = np.random.normal(0, 100, 100)
    y = x ** 1.5 + noise
    df = pd.DataFrame({'x': x, 'y': y})
    df = df.sort_values('x').reset_index(drop=True)
    return df



"""
Create a function 'plot_data' that plots the data points from the data frame returned by 'gendatapoints'.
Arguments:
- 'data' is a pandas data frame with two columns, 'x' and 'y'.
Returns:
- None.
Details:
- The data points are plotted as a scatter plot.
- The plot has a title 'Data Points', x-axis label 'x', and y-axis label 'f(x)'.
"""

def plot_data(data):
    plt.scatter(data['x'], data['y'])
    plt.title('Data Points')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.show()

"""
Create a function 'main' that generates data points and plots them.
Arguments:
- None
Returns:
- None
"""

def main():
    data = gendatapoints((0, 100))
    plot_data(data)

if __name__ == '__main__':
    main()