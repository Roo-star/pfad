import pandas as pd

# Data Source URL
url = "https://berkeley-earth-temperature-hr.s3.amazonaws.com/Global_TAVG_monthly.txt"

# Read data files,skipping comment lines starting with '%'
data = pd.read_csv(url, delim_whitespace=True, comment='%', header=None, 
                   names=['Year', 'Month', 'Monthly_Anomaly', 'Monthly_Uncertainty', 
                          'Annual_Anomaly', 'Annual_Uncertainty', 'Five_Year_Anomaly', 
                          'Five_Year_Uncertainty', 'Ten_Year_Anomaly', 
                          'Ten_Year_Uncertainty', 'Twenty_Year_Anomaly', 
                          'Twenty_Year_Uncertainty'])

# Save all the data as CSV file
data.to_csv("global_temperature_data_1850_present.csv", index=False)

# Check the first 5 rows of data
print(data.head())
