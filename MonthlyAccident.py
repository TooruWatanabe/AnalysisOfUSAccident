import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("MonthlyAccident.csv")

# Convert 'YearMonth' to datetime format for proper sorting
df['YearMonth'] = pd.to_datetime(df['YearMonth'])

# Filter data for the required time range (February 2016 to March 2023)
filtered_df = df[(df['YearMonth'] >= '2016-02') & (df['YearMonth'] <= '2023-03')]

# Group by 'YearMonth' and sum the 'OccurrenceCount'
monthly_occurrence = filtered_df.groupby('YearMonth')['OccurrenceCount'].sum().reset_index()

# Plotting the bar graph
plt.figure(figsize=(12, 6))
plt.bar(monthly_occurrence['YearMonth'], monthly_occurrence['OccurrenceCount'], color='blue')
plt.xlabel('Year-Month')
plt.ylabel('OccurrenceCount')
plt.title('Monthly Occurrence Count from February 2016 to March 2023')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
