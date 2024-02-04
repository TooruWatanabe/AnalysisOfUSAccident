import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
file_path = "StateWiseAccident.csv"
df = pd.read_csv(file_path, delimiter='\t')


# Separate the combined column into 'State' and 'COUNT("State")'
df[['State', 'COUNT("State")']] = df['State,"COUNT(""State"")"'].str.split(',', expand=True)

# Print the column names to verify the separation
print(df.columns)

# Plotting the bar chart
plt.figure(figsize=(10, 6))
plt.bar(df['State'], df['COUNT("State")'].astype(int))
plt.xlabel('State')
plt.ylabel('Number of Accidents')
plt.title('Number of Accidents in Each State')
plt.show()
