import matplotlib.pyplot as plt
import pandas as pd

# Loading the cleaned data
cleaned_data = pd.read_csv('../clean_data/cleaned_female_participants_data.csv')

# Visualization height distribution
plt.hist(cleaned_data['Height'], bins=10, color='skyblue', edgecolor='black')
plt.xlabel('Height (inches)')
plt.ylabel('Frequency')
plt.title('Distribution of Height')
plt.show()

#  relationship between age and grip strength
plt.scatter(cleaned_data['Age'], cleaned_data['Grip_strength'], color='orange')
plt.xlabel('Age (years)')
plt.ylabel('Grip Strength (pounds)')
plt.title('Relationship between Age and Grip Strength')
plt.show()

#  frailty distribution
frailty_counts = cleaned_data['Frailty'].value_counts()
plt.bar(frailty_counts.index, frailty_counts.values, color=['green', 'red'])
plt.xlabel('Frailty')
plt.ylabel('Count')
plt.title('Distribution of Frailty')
plt.xticks([0, 1], ['No', 'Yes'])
plt.show()