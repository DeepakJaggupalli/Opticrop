import os
import urllib.request
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Create directories
os.makedirs('plots', exist_ok=True)
os.makedirs('models', exist_ok=True)

print("1. Downloading dataset...")
url = 'https://raw.githubusercontent.com/gabbygab1233/Crop-Recommender/main/Crop_recommendation.csv'
file_path = 'Crop_recommendation.csv'
if not os.path.exists(file_path):
    urllib.request.urlretrieve(url, file_path)
    print("Dataset downloaded successfully.")
else:
    print("Dataset already exists.")

print("\n2. Reading the Dataset...")
df = pd.read_csv(file_path)
print(f"Shape of the dataset: {df.shape}")
print(df.head())

print("\n3. Checking for Null Values...")
print(df.isnull().sum())

print("\n4. Handling Outliers (Skipping removal to preserve crop specifics, but we can visualize)")
# We'll visualize outliers using boxplots
plt.figure(figsize=(15, 10))
sns.boxplot(data=df.drop('label', axis=1))
plt.title("Boxplot of Features")
plt.savefig('plots/outliers_boxplot.png')
plt.close()

print("\n5. Extracting Seasonal Crops")
# Group crops by their average temperature and rainfall requirements
seasonal_summary = df.groupby('label')[['temperature', 'rainfall']].mean().sort_values(by='temperature')
print(seasonal_summary)

print("\n6. Exploratory Data Analysis (EDA)")
# Univariate Analysis
plt.figure(figsize=(10, 6))
sns.histplot(df['temperature'], kde=True, color='red')
plt.title('Temperature Distribution')
plt.savefig('plots/univariate_temperature.png')
plt.close()

# Bivariate Analysis
plt.figure(figsize=(10, 6))
sns.scatterplot(x='temperature', y='humidity', hue='label', data=df, legend=False)
plt.title('Temperature vs Humidity')
plt.savefig('plots/bivariate_temp_humidity.png')
plt.close()

# Multivariate Analysis (Correlation Heatmap)
plt.figure(figsize=(10, 8))
# Select only numeric columns for correlation
numeric_cols = df.select_dtypes(include=[np.number])
sns.heatmap(numeric_cols.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.savefig('plots/multivariate_correlation.png')
plt.close()
print("Plots saved in 'plots/' directory.")

print("\n7. Splitting Data into Train and Test Sets")
X = df.drop('label', axis=1)
y = df['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"X_train shape: {X_train.shape}, X_test shape: {X_test.shape}")

print("\n8. K-Means Clustering (Unsupervised grouping based on environmental needs)")
# Using K-Means to cluster crops into 4 broad categories (e.g., Summer, Winter, Monsoon, Spring crops)
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
df['cluster'] = kmeans.fit_predict(numeric_cols)
print("Cluster Centers (N, P, K, Temp, Hum, pH, Rain):")
print(kmeans.cluster_centers_)

print("\n9. Logistic Regression (Supervised Modeling)")
model = LogisticRegression(max_iter=5000, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"Logistic Regression Accuracy: {acc*100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\n10. Evaluating Model Performance and Saving the Best Model")
joblib.dump(model, 'models/model.pkl')
print("Model saved to 'models/model.pkl'")

print("\n11. Predict the Best Crop Based on Given Parameters (Test)")
# Sample input: N=90, P=42, K=43, Temp=20.8, Hum=82, pH=6.5, Rain=202 (Expected: Rice)
sample_input = np.array([[90, 42, 43, 20.8, 82, 6.5, 202]])
prediction = model.predict(sample_input)
print(f"Sample Input {sample_input[0]}")
print(f"Predicted Crop: {prediction[0]}")

print("\nPipeline execution complete.")
