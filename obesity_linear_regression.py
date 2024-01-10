import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Assuming your dataset has columns 'Sample_Size' and 'High_Confidence_Limit'
csv_file_path = 'Nutrition__Physical_Activity__and_Obesity_-_Behavioral_Risk_Factor_Surveillance_System.csv'
dataset = pd.read_csv(csv_file_path)

# Drop rows with null values in 'Sample_Size' or 'High_Confidence_Limit'
dataset = dataset.dropna(subset=['Sample_Size', 'High_Confidence_Limit '])

# Extracting data
sample_sizes = dataset['Sample_Size']
high_confidence_limits = dataset['High_Confidence_Limit ']

# Calculate coefficients of the linear regression line manually
mean_x = np.mean(sample_sizes)
mean_y = np.mean(high_confidence_limits)
numerator = np.sum((sample_sizes - mean_x) * (high_confidence_limits - mean_y))
denominator = np.sum((sample_sizes - mean_x) ** 2)
slope = numerator / denominator
intercept = mean_y - slope * mean_x

# Predict high confidence limits based on the manually calculated linear regression model
predicted_values = slope * sample_sizes + intercept

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(sample_sizes, high_confidence_limits, color='blue', alpha=0.5, label='Data Points', s=1)
plt.plot(sample_sizes, predicted_values, color='black', linewidth=1, label='Linear Regression Line')
plt.title('Scatter Plot with Linear Regression Line')
plt.xlabel('Sample Size')
plt.ylabel('High Confidence Limit')
plt.grid(True)
plt.legend()
plt.show()
