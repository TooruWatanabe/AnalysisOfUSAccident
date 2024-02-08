import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("MonthlyAccidentDetail.csv")

# Convert YearMonth column to datetime
df['YearMonth'] = pd.to_datetime(df['YearMonth'])

# Extract year from YearMonth
df['Year'] = df['YearMonth'].dt.year

# Filter data for the years 2017 to 2022
df = df[df['Year'].between(2017, 2022)]

# Group by Year and sum the severity counts
severity_counts = df.groupby('Year')[['Severity_1', 'Severity_2', 'Severity_3', 'Severity_4']].sum()

# Plot the stacked bar chart
severity_counts.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Monthly Accident Severity Counts from 2017 to 2022')
plt.xlabel('Year')
plt.ylabel('Number of Occurrences')
plt.xticks(rotation=45)
plt.legend(title='Severity')
plt.tight_layout()
plt.show()
