import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

# Load the CSV file
df = pd.read_csv('50SOC_asym_15to40.csv')

# Assuming the unnamed column is the first column and represents datetime
df.rename(columns={df.columns[0]: 'Datetime'}, inplace=True)

# Convert the 'Datetime' column to datetime objects
df['Datetime'] = pd.to_datetime(df['Datetime'])

# Calculate the time in seconds since the first time in the data
df['Time (s)'] = (df['Datetime'] - df['Datetime'].min()).dt.total_seconds()

# Plot temperature as a function of time
plt.figure(figsize=(12, 6))
for col in df.columns[2:7]:  # Columns for temperature data
    plt.plot(df['Time (s)'], df[col], label=col)
plt.xlabel('Time (s)')
plt.ylabel('Temperature (C)')
plt.title('Temperature as a function of time')
plt.legend()
plt.grid(True)
plt.show()

# Plot heat flux as a function of time
plt.figure(figsize=(12, 6))
for col in df.columns[7:9]:  # Columns for heat flux data
    plt.plot(df['Time (s)'], df[col], label=col)
plt.xlabel('Time (s)')
plt.ylabel('Heat Flux (V)')
plt.title('Heat Flux as a function of time')
plt.legend()
plt.grid(True)
plt.show()

# Function to calculate averages within a time interval and print them
E1_calibration = [17.23,0.0215] # S0, Sc
E2_calibration = [19.63,0.0245] # S0, Sc
def calculate_flux(V, T_S, S0, Sc, T_0 = 22.5):
    sensitivity = S0 + (T_S - T_0) * Sc
    return 1000*1000*V/sensitivity

def calculate_and_print_averages(df, start_time, end_time, T_left, T_right):
    # Filter the dataframe for the given time interval
    interval_df = df[(df['Time (s)'] >= start_time) & (df['Time (s)'] <= end_time)]
    
    # Calculate averages for T1, T5, E1 flux, and E2 flux
    avg_T1 = interval_df['T1 Last (C)'].mean()
    avg_T5 = interval_df['T5 Last (C)'].mean()
    avg_E1_flux = calculate_flux(interval_df['E1 flux Last (V)'].mean(), T_left, E1_calibration[0], E1_calibration[1])
    avg_E2_flux = calculate_flux(interval_df['E2 flux Last (V)'].mean(), T_right, E2_calibration[0], E2_calibration[1])
    
    # Print the averages
    # print(f"Averages from {start_time} to {end_time} seconds:")
    print(f"Average T1: {round(avg_T1, 3)} C")
    print(f"Average T5: {round(avg_T5, 3)} C")
    print(f"Average E1 flux: {round(avg_E1_flux, 2)} W/m^2")
    print(f"Average E2 flux: {round(avg_E2_flux, 2)} W/m^2")
    
    print("x: "+str(np.linspace(0, 300, 5).tolist()))
    print("T: ["+str(interval_df['T1 Last (C)'].mean())+", "+str(interval_df['T2 Last (C)'].mean())+", "+str(interval_df['T3 Last (C)'].mean())+", "+str(interval_df['T4 Last (C)'].mean())+", "+str(interval_df['T5 Last (C)'].mean())+"]")
    print("Average of the five temperatures: "+str(round(np.mean([interval_df['T1 Last (C)'].mean(),interval_df['T2 Last (C)'].mean(),interval_df['T3 Last (C)'].mean(),interval_df['T4 Last (C)'].mean(),interval_df['T5 Last (C)'].mean()]),2)))

# # Example usage of calculate_and_print_averages function
print("15 degrees")
calculate_and_print_averages(df, 10000, 11000, 15, 15)
print("15 and 20 degrees")
calculate_and_print_averages(df, 46000, 47000, 15, 20)
print()
print("20 degrees")
calculate_and_print_averages(df, 73000, 74000, 20, 20)
print()
print("20 and 25 degrees")
calculate_and_print_averages(df, 108000, 109000, 20, 25)
print()
print("25 degrees")
calculate_and_print_averages(df, 136000, 137000, 25, 25)
print("25 and 30 degrees")
calculate_and_print_averages(df, 186000, 187000, 25, 30)
print()
print("30 degrees")
calculate_and_print_averages(df, 231000, 232000, 30, 30)
print("30 and 35 degrees")
calculate_and_print_averages(df, 282000, 283000, 30, 35)
print()
print("35 degrees")
calculate_and_print_averages(df, 312000, 313000, 35, 35)
print("35 to 40 degrees")
calculate_and_print_averages(df, 344000, 345000, 35, 40)
print("40 degrees")
calculate_and_print_averages(df, 375000, 376000, 40, 40)