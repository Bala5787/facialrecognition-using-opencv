import pandas as pd
import numpy as np
import matplotlib

import matplotlib.pyplot as plt


# Load the CSV file
s = pd.read_csv('2024-05-26.csv')

# Extract columns as numpy arrays
data = s.iloc[:, 0].values
data2 = s.iloc[:, 1].values

def to1d(array):
    """Convert a 2D array to a 1D list with unique elements."""
    return list(pd.unique(array))

# Convert data to 1D lists with unique elements
r1 = to1d(data)
r2 = to1d(data2)

print(r1)
print(r2)

# Ensure both lists have the same length
l1 = len(r1)
l2 = len(r2)
print(l1, l2)

if l2 < l1:
    d = l1 - l2
    print(d)
    r2.extend([r2[-1]] * d)

print(r2)

# Plotting
plt.title('Name vs Time of Entry')
plt.xlabel('Name')
plt.ylabel('Time of Entry')

plt.plot(r1, r2, marker='o')  # Added marker for better visualization
plt.xticks(rotation=90)       # Rotate x labels if they are dates
plt.tight_layout()            # Adjust layout to fit everything
plt.savefig('plot.png')
plt.show()

