import pandas as pd
from sklearn.preprocessing import LabelEncoder


# Load the dataset
data = pd.read_csv('../raw_data/StudentsPerformance.csv')

# Check for missing values
missing_values = data.isnull().sum()
print("Missing Values:")
print(missing_values)

#No missing values found

# Check data types
print("\nData Types:")
print(data.dtypes)

# Ensure all column names are consistent and formatted properly
data.columns = data.columns.str.lower().str.replace(' ', '_')

# Display the first few rows of the dataset
print("\nFirst few rows of the dataset:")
print(data.head())

# Encode 'test preparation course' column
#'none' is encoded as 0 and 'completed' is encoded as 1
encoder = LabelEncoder()
data['test_preparation_course'] = encoder.fit_transform(data['test_preparation_course'])


# Save the cleaned dataset
data.to_csv('../cleaned_data/cleaned_StudentPerformance.csv', index=False)
