import pandas as pd

# Load raw data
raw_data = pd.read_csv('../raw_data/female_participants_data.csv')


# Data Cleaning
#missing_values = raw_data.isnull().sum()
# Check for missing values (not needed for this small example)

# Data Transformation

# Rename columns
raw_data.columns = ['Height', 'Weight', 'Age', 'Grip_strength', 'Frailty']

# Convert grip strength from kilograms to pounds
raw_data['Grip_strength'] *= 2.204

# Round grip strength values to 2 decimals
raw_data['Grip_strength'] = raw_data['Grip_strength'].round(2)

#converting Char Y and N to integers 1 and 0
raw_data['Frailty'] = raw_data['Frailty'].str.strip().map({'Y': 1, 'N': 0})


#printing sample 
print(raw_data.head())

# Save cleaned and transformed data

raw_data.to_csv('../clean_data/cleaned_female_participants_data.csv', index=False, encoding='utf-8')
