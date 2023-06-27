import pandas as pd

df = pd.read_csv('input.csv')

df = df.drop_duplicates()

df.to_csv('output.csv', index=False)

# Read the CSV file into a DataFrame
df = pd.read_csv('your_file.csv')

# Identify and remove duplicate entries
duplicates = df.duplicated(subset=['name', 'iban'], keep='first')
df_cleaned = df[~duplicates].copy()

# Assign unique 'id' to any duplicated rows
duplicate_indices = duplicates[duplicates].index
df_cleaned.loc[duplicate_indices, 'id'] = range(len(duplicate_indices))

# Save the cleaned DataFrame to a new CSV file
df_cleaned.to_csv('cleaned_file.csv', index=False)

