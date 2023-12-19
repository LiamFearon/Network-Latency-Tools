import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('ping_times.csv')

# Create a line plot of ping times
plt.figure(figsize=(10, 6))
plt.plot(df['PingTime'])
plt.xlabel('Ping Number')
plt.ylabel('Ping Time (ms)')
plt.title('Ping Time Over Time')
plt.grid(True)
plt.show()