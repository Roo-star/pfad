import pandas as pd

# Reading CSV files
data = pd.read_csv("global_temperature_data_1850_present.csv")

# Create a date column to facilitate time series of visualization
data['Date'] = pd.to_datetime(data[['Year', 'Month']].assign(DAY=1))

# Check the first few lines of data to make sure they are ready correctly
print(data.head())
