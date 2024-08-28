import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset (assuming it's in a CSV file)
df = pd.read_csv('titanic.csv')

# Print the number of rows before cleaning
print(f"Number of rows before cleaning: {df.shape[0]}")

# Drop rows with missing values
df_cleaned = df.dropna()

# Print the number of rows after cleaning
print(f"Number of rows after cleaning: {df_cleaned.shape[0]}")

# Group the data by gender and survival status
grouped_data = df_cleaned.groupby(['Sex', 'Survived']).size().unstack()

# Create the stacked bar chart
grouped_data.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Titanic Survival by Gender and Class')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.legend(['Deceased', 'Survived'])
plt.show()