import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

csv_file_path = 'Life Expectancy Data.csv'
dataset = pd.read_csv(csv_file_path)

# Drop rows with null values in 'Life expectancy' or 'Schooling'
dataset = dataset.dropna(subset=['Life expectancy ', 'Schooling'])

# Extracting data
life_expectancy = dataset['Life expectancy ']
schooling_years = dataset['Schooling']

# Calculate coefficients of the linear regression line manually
mean_x = np.mean(schooling_years)
mean_y = np.mean(life_expectancy)
numerator = np.sum((schooling_years - mean_x) * (life_expectancy - mean_y))
denominator = np.sum((schooling_years - mean_x) ** 2)
slope = numerator / denominator
intercept = mean_y - slope * mean_x

# Predict life expectancy based on the manually calculated linear regression model
predicted_values = slope * schooling_years + intercept

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(schooling_years, life_expectancy, color='blue', alpha=0.5, label='Data Points', s=2)
plt.plot(schooling_years, predicted_values, color='black', linewidth=1, label='Linear Regression Line')
plt.title('Schooling on Life Expectancy')
plt.xlabel('Schooling Years')
plt.ylabel('Life Expectancy')
plt.grid(True)
plt.legend()
plt.show()
