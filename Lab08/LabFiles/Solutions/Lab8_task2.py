#####
# Lab8: Task 2
#####

# load libraries

import numpy as np
# import pandas
import pandas as pd
# Import Decision Tree Classifier
from sklearn.tree import DecisionTreeClassifier 
# Import train_test_split function
from sklearn.model_selection import train_test_split 
#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics

# loading data

df2 = pd.read_csv("diabetes_with_head.csv")
print(df2.shape)

df2.head()

# check the type of data
print(df2.dtypes)

# check duplicate rows
duplicate_rows = df2[df2.duplicated()]
print("number of duplicate rows: ", duplicate_rows.shape)

# print summary statictics
print(df2.describe())

# dispaly the first 10 rows
print(df2.head(10))

# Count the number of null values in each column
print(df2.isnull().sum())

# count of the number of missing values on each of these columns
print((df2[["glucose","bp","skin","insulin","BMI"]] == 0).sum())

# mark zero values as missing (with the value of NaN)
df2[["glucose","bp","skin","insulin","BMI"]] = df2[["glucose","bp","skin","insulin","BMI"]].replace(0, np.NaN)
# check the number of NaN values in each column
print(df2.isnull().sum())
# print the first 10 rows of data
print(df2.head(10))

# fill missing values with mean column values
df2.fillna(df2.mean(), inplace=True)
# check if there is still any NaN values in the dataset
print(df2.isnull().sum())
# check the imputated the first 10 rows of data
print(df2.head(10))

# Finding the correlations between the variables.
plt.figure(figsize=(20,10))
corl= df2.corr()
sns.heatmap(corl,cmap="BrBG",annot=True)
print(corl)

#split dataset into input variable X and target variable y

X = df2.drop(['label'], axis=1)

#check that the class variable has been removed
X.head()

#separate target variable
y = df2.label

#view target values
print(y[0:5])

# Split dataset into training set and test set:  70% training and 30% testing
X_train, X_Vali_test, y_train, y_Vali_test = train_test_split(X, y, test_size=0.3, random_state=1) 

print(X_train.shape)

# Create Decision Tree classifier object
clf = DecisionTreeClassifier()

# Train Decision Tree Classifier
clf = clf.fit(X_train,y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_Vali_test)

# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_Vali_test, y_pred))

from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

feature_cols = ['pregnant', 'glucose','bp','skin','insulin', 'bmi','pedigree', 'age']

plt.figure(figsize=(25,12))
a = plot_tree(clf, 
              feature_names=feature_cols, 
              class_names=['0','1'], 
              filled=True, 
              rounded=True,
              fontsize = 5)
for o in a:
    arrow = o.arrow_patch
    if arrow is not None:
        arrow.set_edgecolor('black')
        arrow.set_linewidth(2)

# Create Decision Tree classifier object
clf_02 = DecisionTreeClassifier(criterion="entropy", max_depth=3)

# Train Decision Tree Classifer
clf_02 = clf_02.fit(X_train,y_train)

#Predict the response for test dataset
y_pred = clf_02.predict(X_Vali_test)

# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_Vali_test, y_pred))

plt.figure(figsize=(25,10))
a = plot_tree(clf_02, 
              feature_names=feature_cols, 
              class_names=['0','1'], 
              filled=True, 
              rounded=True,
              fontsize = 14)
for o in a:
    arrow = o.arrow_patch
    if arrow is not None:
        arrow.set_edgecolor('black')
        arrow.set_linewidth(2)
