"""This file generates random pseudo data into CSV file to test this program."""

import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Create a DataFrame with 200 rows and 20 columns
n_rows = 200
n_cols = 20
columns = [f"feature_{i+1}" for i in range(n_cols)]

# Generate random normal data
data = np.random.randn(n_rows, n_cols)

# Introduce ~10% missing values randomly
mask = np.random.rand(n_rows, n_cols) < 0.1
data[mask] = np.nan

# Create DataFrame
df = pd.DataFrame(data, columns=columns)

# Save the file
output_file = "simulated_missing_data.csv"
df.to_csv(output_file, index=False)

print(f"Simulated data saved to {output_file}")