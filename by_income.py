import pandas as pd
import matplotlib.pyplot as plt

csv_file_path = 'Nutrition__Physical_Activity__and_Obesity_-_Behavioral_Risk_Factor_Surveillance_System.csv'
dataset = pd.read_csv(csv_file_path)

# Filter and process data
filtered_data = dataset[['Income', 'Data_Value']].dropna()
average_income_data = filtered_data.groupby('Income')['Data_Value'].mean().reset_index()

# Plotting
plt.figure(figsize=(12, 5))
bar_plot = plt.bar(average_income_data['Income'], average_income_data['Data_Value'], color='orange')

# Axes labels and title
plt.xlabel('Income Groups')
plt.ylabel('Average Obesity Percentage')
plt.title('Average Obesity Percentage by Income Group')

# Adjust x-axis tick labels rotation, alignment, and font size
plt.xticks(rotation=0, ha='center', fontsize=6)

# Display values on top of bars for better clarity
for bar in bar_plot:
    bar_height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, bar_height + 0.01, round(bar_height, 2),
             ha='center',
             va='bottom',
             fontsize=6,
             color='black')

plt.show()
