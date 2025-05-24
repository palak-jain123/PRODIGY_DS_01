# -*- coding: utf-8 -*-
"""
Created on Sat May 24 16:49:48 2025

@author: jainp
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset (skip header rows)
file_path = 'API_SP.POP.TOTL_DS2_en_csv_v2_85220.csv'
df = pd.read_csv(file_path, skiprows=4)

# Extract only necessary columns
df_pop = df[['Country Name', '2023']].dropna()
df_pop.columns = ['Country', 'Population_2023']

# Sort by population in descending order and take top 20
top20 = df_pop.sort_values(by='Population_2023', ascending=False).head(20)

# Plot the bar chart
plt.figure(figsize=(12, 8))
plt.barh(top20['Country'][::-1], top20['Population_2023'][::-1], color='skyblue')
plt.xlabel('Population')
plt.title('Top 20 Most Populous Countries (2023)')
plt.tight_layout()

# Save and show
plt.savefig('top_20_population_2023.png')
plt.show()