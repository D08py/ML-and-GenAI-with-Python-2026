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
#ques:1 load the dataset and display the first five records
df=pd.read_csv("Dataset 2.csv")
print(df.head(5)) #with only df.head() same result
#ques:2 Determine the number of rows and column in the dataset
print("number of columns:",len(df.columns))
print("number of rows:",df.shape[0])
#qyes 3: Display all column name
print(df.columns)
#identify numerical and categorical features
# Numerical columns
numerical_features = df.select_dtypes(include=['int64', 'float64']).columns
print("Numerical Features:")
print(numerical_features)

# Categorical columns
categorical_features = df.select_dtypes(include=['object']).columns
print("\nCategorical Features:")
print(categorical_features)
#check whether the  dataset containmissing value
print(df.isna())
#PART B
#EXPLORATORY DATA ANALYSIS
#Ques 6 calculatwe the averagw age of users
print("average age:", round(df['Age'].mean()))
#Ques 7 average watch hours per week
print("average watch hours per week",round(df['WatchHoursPerWeek'].mean()))
# Ques 8 Find the Average monthyly spending of users
print("Average monthly spending of users",round(df["MonthlySpend"].mean()))
# Ques 9 count the number of users in each subscription category
print(df['SubscriptionType'].value_counts())
#Ques 10 Determine the percentage of users who renewed their subscription
renewed_percentage = (df['SubscriptionRenewed'] == 'Yes').mean() * 100
print("Percentage of users who renewed their subscription:", renewed_percentage, "%")
#PART C
#DATA PREPARATION
#Ques 11 Convert categorical features into numerical form
le=LabelEncoder()
df['Gender']=le.fit_transform(df['Gender'])
df['SubscriptionType']=le.fit_transform(df['SubscriptionType'])
df['FavoriteGenre']=le.fit_transform(df['FavoriteGenre'])
df['SubscriptionRenewed']=le.fit_transform(df['SubscriptionRenewed'])
#Ques 12 Define the feature set(X) and target variable (y) for subscription renewable pridiction.
# Feature set (X)
X = df.drop('SubscriptionRenewed', axis=1)

# Target variable (y)
y = df['SubscriptionRenewed']

print("Features (X):")
print(X.head())

print("\nTarget (y):")
print(y.head())
#Ques 13 split the dataset into training and testing test
from sklearn.model_selection import train_test_split

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,      # 20% testing, 80% training
    random_state=42     # for reproducibility
)

print("Training features shape:", X_train.shape)
print("Testing features shape:", X_test.shape)
print("Training target shape:", y_train.shape)
print("Testing target shape:", y_test.shape)
#PART D
#DECISION TREE CLASSIFICATION
#Ques 14 Train a Decision Tree model To predict Whether a user will renew ther subscription
#Ques 15 #Evaluate the model using accuracy 
#Ques 16 Generate and interpret the confusion matrix
X = df.drop(['UserID', 'MonthlySpend', 'SubscriptionRenewed'], axis=1)
y = df['SubscriptionRenewed']
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)
dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train, y_train)
pred = dt.predict(X_test)
print("Decision Tree Accuracy:", accuracy_score(y_test, pred))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, pred))
#PART E
#K-Nearest Neighbour(KNN)
#Ques 17 Train a KNN CLASSIFIER WITH K=5
knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train,y_train)
knn_pred=knn.predict(X_test)
print('KNN Accuracy:',accuracy_score(y_test,knn_pred))
#Ques 18 compare the accuracy of knn with decion tree
#PART F LINEAR REGRESSION
#Ques 19 Train a Linear Regression model to predict monthly spending
#Ques 20 Predict the monthly spending for a new user and interpret the result
X_reg = df.drop(['UserID', 'MonthlySpend', 'SubscriptionRenewed'], axis=1)
y_reg = df['MonthlySpend']
X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(
    X_reg, y_reg,
    test_size=0.2,
    random_state=42
)
lr=LinearRegression()
lr.fit(X_train_reg,y_train_reg)
amount = lr.predict([[30, 1, 1, 20, 3, 2, 10]])
print("Predicted Spending:", amount[0])
print('Predicted Spending:',amount[0])