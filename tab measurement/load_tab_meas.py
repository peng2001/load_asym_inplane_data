import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('tab_k_test_2.csv')

# Assuming the unnamed column is the first column and represents datetime
df.rename(columns={df.columns[0]: 'Datetime'}, inplace=True)

# Convert the 'Datetime' column to datetime objects
df['Datetime'] = pd.to_datetime(df['Datetime'])

# Calculate the time in seconds since the first time in the data
df['Time (s)'] = (df['Datetime'] - df['Datetime'].min()).dt.total_seconds()

# Plot heat flux as a function of time
plt.figure(figsize=(12, 6))
plt.plot(df['Time (s)'], df["E2 flux Last (V)"], label="Heat Flux E2")
plt.xlabel('Time (s)')
plt.ylabel('Heat Flux (V)')
plt.title('Heat Flux as a function of time')
plt.legend()
plt.grid(True)
plt.show()

E2_calibration = [19.63,0.0245] # S0, Sc

def calculate_flux(V, T_S, S0, Sc, T_0 = 22.5):
    sensitivity = S0 + (T_S - T_0) * Sc
    return 1000*1000*V/sensitivity

def calculate_and_print_averages(df, start_time, end_time, temperature_E2): # in this experiment, T2 corresponds to the heat flux sensor
    # Filter the dataframe for the given time interval
    interval_df = df[(df['Time (s)'] >= start_time) & (df['Time (s)'] <= end_time)]
    
    # Calculate averages for E2 flux
    avg_flux_E2 = calculate_flux(interval_df['E2 flux Last (V)'].mean(), T_S=temperature_E2, S0=E2_calibration[0], Sc=E2_calibration[1])
    print("Average flux in time "+str(start_time)+" to "+str(end_time)+": "+str(round(avg_flux_E2,3))+" W/m^2")
    

# Example usage of calculate_and_print_averages function
# copper
# print("loss: ")
# calculate_and_print_averages(df, 130000,165000, 25)
# calculate_and_print_averages(df, 5000,6000, 27.5)
# calculate_and_print_averages(df, 9000,12000, 22.5)
# calculate_and_print_averages(df, 13000,14500, 30)
# calculate_and_print_averages(df, 16000,18400, 20)
# print()
# calculate_and_print_averages(df, 20000,70000, 27.5)
# calculate_and_print_averages(df, 82000,85000, 22.5)
# calculate_and_print_averages(df, 92000,98000, 30)
# calculate_and_print_averages(df, 100000,105000, 20)
# print()
# calculate_and_print_averages(df, 106000,109000, 27.5)
# calculate_and_print_averages(df, 110000,113000, 22.5)
# calculate_and_print_averages(df, 115000,121000, 30)
# calculate_and_print_averages(df, 123000,125500, 20)

# grey side
print("loss: ")
calculate_and_print_averages(df, 500,2000, 25)
calculate_and_print_averages(df, 4000,20000, 27.5)
calculate_and_print_averages(df, 23500,26500, 22.5)
calculate_and_print_averages(df, 27000,31500, 30)
calculate_and_print_averages(df, 33000,35000, 20)
print()
calculate_and_print_averages(df, 37000,72000, 27.5)
calculate_and_print_averages(df, 74000,83000, 22.5)
calculate_and_print_averages(df, 84000,88000, 30)
calculate_and_print_averages(df, 90000,99000, 20)
print()
calculate_and_print_averages(df, 100000,124000, 27.5)
calculate_and_print_averages(df, 126000,161000, 22.5)
calculate_and_print_averages(df, 162500,174000, 30)
calculate_and_print_averages(df, 175000,195000, 20)