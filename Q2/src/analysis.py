import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import seaborn as sns
# Load the dataset
data = pd.read_csv('../cleaned_data/cleaned_StudentPerformance.csv')



#Co relation analysis
# Compute correlation matrix
correlation_matrix = data[['math_score', 'reading_score', 'writing_score']].corr()


# Box plot comparison of scores for students who completed and did not complete the test preparation course
# Bar plot comparison of mean scores for students who completed and did not complete the test preparation course
plt.figure(figsize=(10, 6))
sns.barplot(x='test_preparation_course', y='math_score', data=data, ci=None)
sns.barplot(x='test_preparation_course', y='reading_score', data=data, ci=None)
sns.barplot(x='test_preparation_course', y='writing_score', data=data, ci=None)
plt.title('Comparison of Mean Scores by Test Preparation Course Completion')
plt.xlabel('Test Preparation Course Completion')
plt.ylabel('Mean Score')
plt.legend(['Math Score', 'Reading Score', 'Writing Score'])
plt.show()

#  correlation matrix as a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", square=True)
plt.title('Correlation Matrix of Math, Reading, and Writing Scores')
plt.show()


# Stacked Bar Chart of Race/Ethnicity and Scores
plt.figure(figsize=(10, 6))
sns.barplot(x='race/ethnicity', y='math_score', data=data, ci=None)
sns.barplot(x='race/ethnicity', y='reading_score', data=data, ci=None)
sns.barplot(x='race/ethnicity', y='writing_score', data=data, ci=None)
plt.title('Stacked Bar Chart of Race/Ethnicity and Scores')
plt.ylabel('Mean Score')
plt.xlabel('Race/Ethnicity')
plt.legend(['Math Score', 'Reading Score', 'Writing Score'])
plt.show()

#  Histogram of Math Scores
plt.figure(figsize=(8, 6))
sns.histplot(data['math_score'], bins=10, kde=True)
plt.title('Histogram of Math Scores')
plt.xlabel('Math Score')
plt.ylabel('Frequency')
plt.show()

#  Box Plot of Reading Scores by Gender
plt.figure(figsize=(8, 6))
sns.boxplot(x='gender', y='reading_score', data=data)
plt.title('Box Plot of Reading Scores by Gender')
plt.xlabel('Gender')
plt.ylabel('Reading Score')
plt.show()

#  Scatter Plot of Writing Scores vs Math Scores
plt.figure(figsize=(8, 6))
sns.scatterplot(x='math_score', y='writing_score', data=data)
plt.title('Scatter Plot of Writing Scores vs Math Scores')
plt.xlabel('Math Score')
plt.ylabel('Writing Score')
plt.show()

#  Bar Plot of Average Writing Score by Parental Level of Education
plt.figure(figsize=(10, 6))
sns.barplot(x='parental_level_of_education', y='writing_score', data=data, ci=None)
plt.title('Average Writing Score by Parental Level of Education')
plt.xlabel('Parental Level of Education')
plt.ylabel('Average Writing Score')
plt.xticks(rotation=45)
plt.show()

#  Pie Chart of Lunch Type Distribution
lunch_distribution = data['lunch'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(lunch_distribution, labels=lunch_distribution.index, autopct='%1.1f%%', colors=['lightgreen', 'lightblue'])
plt.title('Distribution of Lunch Types')
plt.show()
