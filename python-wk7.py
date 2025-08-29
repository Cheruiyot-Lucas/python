import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris


sns.set(style="whitegrid")


iris_data = load_iris()
df = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
df['species'] = iris_data.target


df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})


print("First 5 rows of the dataset:")
print(df.head())


print("\nDataset Info:")
print(df.info())


print("\nMissing values per column:")
print(df.isnull().sum())


print("\nBasic Statistics of Numerical Columns:")
print(df.describe())


species_group = df.groupby('species').mean()
print("\nMean values for each species:")
print(species_group)


print("\nObservations:")
print("- Setosa has smaller sepal and petal sizes than the other species.")
print("- Virginica has the largest sepal and petal sizes.")
print("- Versicolor is intermediate in size.")


plt.figure(figsize=(8,5))
plt.plot(df['sepal length (cm)'], label='Sepal Length', color='blue')
plt.title('Line Chart: Sepal Length Across Samples')
plt.xlabel('Sample Index')
plt.ylabel('Sepal Length (cm)')
plt.legend()
plt.show()

plt.figure(figsize=(6,4))
sns.barplot(x=species_group.index, y=species_group['petal length (cm)'], palette='viridis')
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')
plt.show()


plt.figure(figsize=(6,4))
plt.hist(df['sepal width (cm)'], bins=10, color='orange', edgecolor='black')
plt.title('Histogram: Sepal Width Distribution')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.show()


plt.figure(figsize=(6,4))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df, palette='deep')
plt.title('Scatter Plot: Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.show()

print("\nSummary of Findings:")
print("1. Setosa flowers are smaller overall compared to Versicolor and Virginica.")
print("2. Virginica has the largest petals and sepals.")
print("3. Positive correlation exists between sepal length and petal length.")
print("4. Distribution of sepal width varies among species, with Setosa being more clustered.")
