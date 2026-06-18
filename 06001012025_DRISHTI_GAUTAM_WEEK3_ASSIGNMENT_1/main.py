"""STUDENT NAME:DRISHTI GAUTAM
ENROLLMENT NUMBER= 06001012025
COLLEGE NAME: IGDTUW
ML AND GEN AI 
WEEK 3 ASSIGNMENT 1"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
#step 1 libraries importing
import numpy as np
#ml algoss
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
knn = KNeighborsClassifier(n_neighbors=5)
# Used to split dataset into training and testing data
from sklearn.model_selection import train_test_split
#used to evaluate classification model
from sklearn.metrics import accuracy_score, confusion_matrix
#convert text columns into numerical values
from sklearn.preprocessing import LabelEncoder
#QUES 1 DATASET OVERVIEW data loading
df=pd.read_csv("d.csv")
#a)how many rows and columns
print("number of columns:",len(df.columns))
print("number of rows:",df.shape[0])
#b)what are the name of all the columns
print(df.columns)
#display the first 10 record
df.head(10)
#DATA TYPE AND MISSING VALUES
#a)check the data type of each column
numerical_features = df.select_dtypes(include=['int64', 'float64']).columns
print("Numerical Features:")
print(numerical_features)
# Categorical columns
categorical_features = df.select_dtypes(include=['object']).columns
print("\nCategorical Features:")
print(categorical_features)
#b)Identify whether any missing values are present. 
print(df.isna())
# c) If missing values exist, mention the affected columns
missing_values = df.isna().sum()
affected_columns = missing_values[missing_values > 0]
if len(affected_columns) > 0:
    print("Columns with missing values:")
    print(affected_columns)
else:
    print("No missing values found in the dataset.")
#QUES 3 Descriptive Statistics 
#Generate summary statistics for all numerical features and answer:
print(df.describe())
#a)Which feature has the highest mean value? 
means = df.mean(numeric_only=True)
highest_mean_feature = means.idxmax()
highest_mean_value = means.max()
print("Feature with highest mean:", highest_mean_feature)
print("Mean value:", highest_mean_value)
#b) Which feature has the highest standard deviation?
std_values = df.std(numeric_only=True)
highest_std_feature = std_values.idxmax()
highest_std_value = std_values.max()
print("Feature with highest standard deviation:", highest_std_feature)
print("Standard deviation:", highest_std_value)
#PART B EXPLORATORY DATA ANALYSIS
#QUES 4 DISTRIBUTION ANALYSIS
"""Create histograms for:
a)rainfall_mm
b)temperature_c
c)fertilizer_kg
d) yield_ton_per_hectare
Write 2–3 observations from each histogram. """
columns = ['rainfall_mm', 'temperature_c', 'fertilizer_kg', 'yield_ton_per_hectare']
for col in columns:
    plt.figure(figsize=(6,4))
    plt.hist(df[col], bins=10)
    plt.title(f'Histogram of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.show()
"""Q5. Crop Type Analysis
a)Find the number of records for each crop type.
b)Create a count plot (bar chart) for crop_type.
c) Which crop appears most frequently?"""
# Q5. Crop Type Analysis
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# 1. Find the number of records for each crop type
crop_counts = df['crop_type'].value_counts()
print("Number of records for each crop type:")
print(crop_counts)
plt.figure(figsize=(8,5))
sns.countplot(x='crop_type', data=df)
plt.title('Count of Records for Each Crop Type')
plt.xlabel('Crop Type')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()
most_frequent_crop = crop_counts.idxmax()
most_frequent_count = crop_counts.max()
print("\nMost Frequent Crop:", most_frequent_crop)
print("Number of Records:", most_frequent_count)
# Q6. Soil Type Analysis
# 1. Find the frequency of each soil type
soil_counts = df['soil_type'].value_counts()
print("Frequency of each soil type:")
print(soil_counts)
# 2. Create a count plot
plt.figure(figsize=(8,5))
sns.countplot(x='soil_type', data=df)
plt.title('Count of Each Soil Type')
plt.xlabel('Soil Type')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()
# 3. Find the most common soil type
most_common_soil = soil_counts.idxmax()
most_common_count = soil_counts.max()
print("\nMost Common Soil Type:", most_common_soil)
print("Number of Records:", most_common_count)
#Q7. Yield Distribution
"""Create a histogram of yield_ton_per_hectare.
Answer:
A)Is the distribution approximately normal?
B)Are there any noticeable outliers?"""
plt.figure(figsize=(8,5))
plt.hist(df['yield_ton_per_hectare'], bins=10)
plt.axvline(df['yield_ton_per_hectare'].mean(),
            linestyle='--',
            label='Mean')
plt.title('Distribution of Yield (ton/hectare)')
plt.xlabel('Yield (ton/hectare)')
plt.ylabel('Frequency')
plt.legend()
plt.show()
#Q8. Scatter Plot Analysis
"""Based on the plots: 
QUES: Which feature appears to have a stronger relationship with yield?  """

# Scatter Plot 1: Rainfall vs Yield
plt.figure(figsize=(6,4))
plt.scatter(df['rainfall_mm'], df['yield_ton_per_hectare'])
plt.title("Rainfall vs Yield")
plt.xlabel("Rainfall (mm)")
plt.ylabel("Yield (ton/hectare)")
plt.grid(True)
plt.show()

# Scatter Plot 2: Fertilizer vs Yield
plt.figure(figsize=(6,4))
plt.scatter(df['fertilizer_kg'], df['yield_ton_per_hectare'])
plt.title("Fertilizer vs Yield")
plt.xlabel("Fertilizer (kg)")
plt.ylabel("Yield (ton/hectare)")
plt.grid(True)
plt.show()
#QUES 9 CORRELATION ANALYSIS
"""Generate a correlation matrix for numerical features.  
Create a heatmap.  
Identify the top three features most correlated with crop yield."""
# Q9. Correlation Matrix and Heatmap
# Select only numerical columns
numerical_df = df.select_dtypes(include=['int64', 'float64'])
# Generate correlation matrix
corr_matrix = numerical_df.corr()
# Display correlation matrix
print("Correlation Matrix:")
print(corr_matrix)
# Create heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix,
            annot=True,
            cmap='coolwarm',
            fmt=".2f",
            linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()
# Find top 3 features most correlated with crop yield
yield_corr = corr_matrix['yield_ton_per_hectare'].drop('yield_ton_per_hectare')
top3 = yield_corr.abs().sort_values(ascending=False).head(3)
print("\nTop 3 Features Most Correlated with Crop Yield:")
print(top3)
#Q10. Group-Based Analysis 
""" Calculate the average yield for: 
a)Each crop type  
b)Each soil type  
Which crop and soil type have the highest average yield? """
# Q10. Average Yield Analysis
# Average yield for each crop type
avg_crop_yield = df.groupby('crop_type')['yield_ton_per_hectare'].mean()
print("Average Yield for Each Crop Type:")
print(avg_crop_yield)
# Average yield for each soil type
avg_soil_yield = df.groupby('soil_type')['yield_ton_per_hectare'].mean()
print("\nAverage Yield for Each Soil Type:")
print(avg_soil_yield)
# Crop type with the highest average yield
highest_crop = avg_crop_yield.idxmax()
highest_crop_yield = avg_crop_yield.max()
print("\nCrop Type with Highest Average Yield:")
print(f"{highest_crop} : {highest_crop_yield:.2f} ton/hectare")
# Soil type with the highest average yield
highest_soil = avg_soil_yield.idxmax()
highest_soil_yield = avg_soil_yield.max()
print("\nSoil Type with Highest Average Yield:")
print(f"{highest_soil} : {highest_soil_yield:.2f} ton/hectare")
#Part C: Data Preparation 
#Q11. Feature Encoding 
"""The dataset contains categorical variables. 
a)Identify the categorical columns.  
b)Convert them into numerical form using One-Hot Encoding.  
c)Display the first five rows of the transformed dataset. """
# Q11. One-Hot Encoding of Categorical Variables
# Identify categorical columns
categorical_cols = df.select_dtypes(include=['object']).columns
print("Categorical Columns:")
print(categorical_cols)
# Apply One-Hot Encoding
df_encoded = pd.get_dummies(df, columns=categorical_cols)
# Display the first five rows of the transformed dataset
print("\nFirst Five Rows of the Transformed Dataset:")
print(df_encoded.head())
#Q12. Feature Selection 
"""Separate: 
a)Input features (X)  
b)Target variable (y)  
Specify which column is being used as the target variable"""
# Q12. Separate Input Features (X) and Target Variable (y)
# Input features (X)
X = df_encoded.drop('yield_ton_per_hectare', axis=1)
# Target variable (y)
y = df_encoded['yield_ton_per_hectare']
# Display the input features
print("Input Features (X):")
print(X.head())
# Display the target variable
print("\nTarget Variable (y):")
print(y.head())
# Display the target column name
print("\nTarget Variable Column:")
print(y.name)
#Part D: Machine Learning 
#Q13. Train-Test Split 
"""Split the dataset into: 
a)80% Training Data  
b)20% Testing Data  
Display the shape of: 
a)X_train  
b) X_test  
c)y_train  
d) y_test  """
# Q13. Split the Dataset into Training and Testing Sets
# Split the dataset into 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)
# Display the shapes
print("Shape of X_train:", X_train.shape)
print("Shape of X_test :", X_test.shape)
print("Shape of y_train:", y_train.shape)
print("Shape of y_test :", y_test.shape)
#Q14. Linear Regression Model
"""a)Train a Linear Regression model.  
b)Display the model coefficients and intercept.  
c)Which feature has the highest positive coefficient?"""
# Q14. Train a Linear Regression Model
# Create and train the model
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
# Display the intercept
print("Intercept:")
print(lr_model.intercept_)
# Display the coefficients
coef_df = pd.DataFrame({
    'Feature': X_train.columns,
    'Coefficient': lr_model.coef_
})
print("\nModel Coefficients:")
print(coef_df)
# Find the feature with the highest positive coefficient
highest_feature = coef_df.loc[coef_df['Coefficient'].idxmax()]
print("\nFeature with Highest Positive Coefficient:")
print(highest_feature)