import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame, specifying the delimiter
df = pd.read_csv("HourlyAccident.csv", delimiter=',')

# Convert the "Hourly" column to datetime format
df['Hourly'] = pd.to_datetime(df['Hourly'], format='%H:%M')

# Extract the hour from the datetime and create a new column "HourOfDay"
df['HourOfDay'] = df['Hourly'].dt.hour

# Convert 'OccurrenceCount' to numeric type
df['OccurrenceCount'] = pd.to_numeric(df['OccurrenceCount'])

# Group by the hour and calculate the sum of "OccurrenceCount"
hourly_counts = df.groupby('HourOfDay')['OccurrenceCount'].sum()

# Create a bar graph
plt.bar(hourly_counts.index, hourly_counts.values)

# Set the labels and title
plt.xlabel('Hour of the Day')
plt.ylabel('Occurrence Count')
plt.title('Hourly Accident Occurrence')

# Show the plot
plt.show()
