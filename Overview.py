import pandas as pd
import re

# Dataset1: Campaign performance data 
# Dataset2: User demographics and behavioral data

ds1 = pd.read_csv('SP25_DA_Capstone_Dataset1.csv', encoding='latin1')
ds2 = pd.read_csv('SP25_DA_Capstone_Dataset2.csv')

print(ds1.info())
print(ds2.info())
print(ds1.head())
print(ds2.head())

print(ds1.isnull().sum())
print(ds2.isnull().sum())

# Dropped Null Values from Dataset1
ds1_cleaned = ds1.dropna()
print(ds1_cleaned.isnull().sum())

# Split 'creative_size.userid' Column
# Created two new columns: 'creative_size' and 'userid'
ds1_cleaned[['creative_size', 'userid']] = ds1_cleaned['creative_size.userid'].str.split('|', expand=True)
ds1_cleaned.to_csv('ds1_cleaned.csv', index=False)
ds1_cleaned = ds1_cleaned.drop(['creative_size.userid'], axis=1)

# Cleaned and standardized user ID formats
ds1_cleaned['userid'] = ds1_cleaned['userid'].astype(str).str.strip().str.upper()
ds2['userid'] = ds2['userid'].astype(str).str.strip().str.upper()

# Merged Cleaned Datasets on 'userid'
merged_df = pd.merge(ds1_cleaned, ds2, on='userid', how='inner')

# Cleaned 'audience_segment' Column
# Removed non-alphanumeric characters
merged_df['audience_segment'] = merged_df['audience_segment'].apply(lambda x: re.sub(r'[^a-zA-Z0-9\s]', '', str(x)))

merged_df.to_csv('Clean/Merged_data.csv', index=False)


