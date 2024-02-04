import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("MonthlyAccident.csv")

# Convert 'YearMonth' to datetime format for proper sorting
df['YearMonth'] = pd.to_datetime(df['YearMonth'])

# Extract year from 'YearMonth'
df['Year'] = df['YearMonth'].dt.year

# Filter data for the required years (2017 to 2022)
filtered_df = df[(df['Year'] >= 2017) & (df['Year'] <= 2022)]

# Group by 'Year' and sum the 'OccurrenceCount'
yearly_occurrence = filtered_df.groupby('Year')['OccurrenceCount'].sum().reset_index()

# Plotting the bar graph
plt.figure(figsize=(10, 6))
plt.bar(yearly_occurrence['Year'], yearly_occurrence['OccurrenceCount'], color='green')
plt.xlabel('Year')
plt.ylabel('OccurrenceCount')
plt.title('Yearly Occurrence Count from 2017 to 2022')
plt.xticks(yearly_occurrence['Year'])
plt.tight_layout()
plt.show()

# Display the tabulated data
print("Yearly Occurrence Count:")
print(yearly_occurrence)
