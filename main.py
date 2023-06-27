import pandas as pd

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


import pandas as pd
from fuzzywuzzy import fuzz

# Read the cleaned CSV file into a DataFrame
df_cleaned = pd.read_csv('cleaned_file.csv')

# Function to calculate string similarity
def calculate_similarity(str1, str2):
    return fuzz.token_set_ratio(str1, str2)  # Use appropriate fuzzy matching algorithm

# Identify and link similar counterparties
linked_counterparties = {}

for i, row in df_cleaned.iterrows():
    unique_counterparty = row['name']  # Use name or iban as the unique identifier

    if unique_counterparty not in linked_counterparties:
        linked_counterparties[unique_counterparty] = []

    for j in range(i + 1, len(df_cleaned)):
        similarity_score = calculate_similarity(unique_counterparty, df_cleaned.loc[j, 'name'])  # Use name or iban
        if similarity_score >= similarity_threshold:
            linked_counterparties[unique_counterparty].append(df_cleaned.loc[j, 'name'])  # Use name or iban

# Create a new DataFrame with linked counterparties
df_linked = pd.DataFrame({'unique_counterparty': linked_counterparties.keys(),
                          'linked_entries': linked_counterparties.values()})

# Save the linked DataFrame to a new CSV file
df_linked.to_csv('linked_file.csv', index=False)



