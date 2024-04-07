import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('funding.csv')
print(data.head())
# Strip leading and trailing whitespace from columns
data = data.map(lambda x: x.strip() if isinstance(x, str) else x)

# Convert the 'Time' column to datetime format
data['Time'] = pd.to_datetime(data['Time'])

# Filter the data for Ethereum
eth_data = data[data['Symbol'] == 'ETHUSD ETH-Margin']

# Convert 'Funding Rate' to float and remove the '%' sign
eth_data['Funding Rate'] = eth_data['Funding Rate'].str.rstrip('%').astype('float')

positive_funding = len(eth_data[eth_data['Funding Rate'] > 0])
print('Number of positive funding rates:', positive_funding)
percentage_positive = round(positive_funding / len(eth_data) * 100, 2)
print(len(eth_data))

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot_date(eth_data['Time'], eth_data['Funding Rate'], linestyle='solid')

plt.title('Ethereum Funding Rates Over Time')
plt.xlabel('Time')
plt.ylabel('Funding Rate')

plt.tight_layout()
plt.axhline(0, color='r', linestyle='--')

# Add the text to the plot
plt.text(0.5, 1.02, f'Percentage of positive funding rate epochs: {percentage_positive:.2f}%', 
         horizontalalignment='center', verticalalignment='top', transform=plt.gca().transAxes, weight='bold')

# Calculate the volatility of the 'Funding Rate'
volatility = eth_data['Funding Rate'].std()

# Add the volatility to the plot
plt.text(0.5, 0.98, f'Volatility of the funding rate: {volatility:.2f}', 
         horizontalalignment='center', verticalalignment='top', transform=plt.gca().transAxes, weight='bold')

plt.show()

plt.savefig('output/funding_rates.png')