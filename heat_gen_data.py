import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('50SOC_1C_heat_gen.csv')

# Assuming the unnamed column is the first column and represents time in HH:MM:SS format
df.rename(columns={df.columns[0]: 'Time'}, inplace=True)

# Convert the 'Time' column to timedelta objects
df['Time'] = pd.to_timedelta(df['Time'])

# Calculate the time in seconds since the first time in the data
df['Time (s)'] = df['Time'].dt.total_seconds()

# Plot temperature as a function of time
plt.figure(figsize=(12, 6))
for col in df.columns[2:5]:  # Columns for temperature data
    plt.plot(df['Time (s)'], df[col], label=col)
plt.xlabel('Time (s)')
plt.ylabel('Temperature (C)')
plt.title('Temperature as a function of time')
plt.legend()
plt.grid(True)
plt.show()

# Function to calculate averages within a time interval and print them

def calculate_and_print_averages(df, start_time, end_time):
    # Filter the dataframe for the given time interval
    interval_df = df[(df['Time (s)'] >= start_time) & (df['Time (s)'] <= end_time)]
    
    # Calculate averages for T1, T5, E1 flux, and E2 flux
    avg_T1 = interval_df['Channel 1 Last (C)'].mean()
    avg_T2 = interval_df['Channel 2 Last (C)'].mean()
    avg_T3 = interval_df['Channel 3 Last (C)'].mean()
    avg_T4 = interval_df['Channel 4 Last (C)'].mean()
    
    # Print the averages
    # print(f"Averages from {start_time} to {end_time} seconds:")
    print(f"Average T1: {round(avg_T1, 3)} C")
    print(f"Average T2: {round(avg_T2, 3)} C")
    print(f"Average T3: {round(avg_T3, 3)} C")
    print(f"Average T4: {round(avg_T4, 3)} C")
    

# Example usage of calculate_and_print_averages function
calculate_and_print_averages(df, 13000,19000)