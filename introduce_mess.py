import pandas as pd
import numpy as np

# Load the clean data
df = pd.read_csv('Sample - Superstore.csv', encoding='latin1')

# 1. Add duplicate rows
duplicates = df.sample(50)
df = pd.concat([df, duplicates])

# 2. Introduce missing values
df.loc[df.sample(100).index, 'Region'] = None
df.loc[df.sample(50).index, 'Postal Code'] = None

# 3. Mess up text formatting
sample_idx = df.sample(200).index
df.loc[sample_idx, 'City'] = df.loc[sample_idx, 'City'].str.upper()

sample_idx2 = df.sample(200).index
df.loc[sample_idx2, 'State'] = df.loc[sample_idx2, 'State'].str.lower()

# 4. Add some negative sales
df.loc[df.sample(30).index, 'Sales'] = -99.99

# Save the messy version
df.to_csv('superstore_messy.csv', index=False)

print(f"Messy dataset created!")
print(f"Total records: {len(df)}")
print(f"Duplicates added: 50")
print(f"Missing values added: 150")
print(f"Formatting issues added: 400")
print(f"Negative sales added: 30")