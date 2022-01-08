# Importing required libraries.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt #visualisation
import seaborn as sns #visualisation

sns.set(color_codes=True)


### Ex_1 
# Load the data into Pandas dataframe and check the number of rows and columns
dataset = pd.read_csv("diabetes.csv", header = None)
print(dataset.shape)


### Ex_2
# check the type of data
print(dataset.dtypes)


### Ex_3
# dispaly the first 10 rows
print(dataset.head(10))


### Ex_4
# check duplicate rows
duplicate_rows = dataset[dataset.duplicated()]
print("number of duplicate rows: ", duplicate_rows.shape)


### Ex_5
# print summary statictics
print(dataset.describe())


### Ex_6
# Count the number of null values in each column
print(dataset.isnull().sum())

# count of the number of missing values on each of these columns
print((dataset[[1,2,3,4,5]] == 0).sum())

# mark zero values as missing (with the value of NaN)
dataset[[1,2,3,4,5]] = dataset[[1,2,3,4,5]].replace(0, np.NaN)
# check the number of NaN values in each column
print(dataset.isnull().sum())
# print the first 10 rows of data
# print(dataset.head(10))

# fill missing values with mean column values
dataset.fillna(dataset.mean(), inplace=True)
# check if there is still any NaN values in the dataset
print(dataset.isnull().sum())
# check the imputated the first 10 rows of data
print(dataset.head(10))


### Ex_7
# plot the histogram of Plasma glucose concentration
plt.figure(0)
plt.hist(dataset[2], bins=20)
plt.title("Histogram of Plasma Glucose concentration")
plt.ylabel('Number of Plasma Glucose concentration')
plt.xlabel('Value of Plasma Glucose concentration');

# plot the histogram of Body mass index
plt.figure(1)
plt.hist(dataset[5], bins=20)
plt.title("Histogram of Body mass index")
plt.ylabel('Number of Body mass index')
plt.xlabel('Value of Body mass index');


### Ex_8
# Finding the correlations between the variables.
plt.figure(figsize=(20,10))
corl= dataset.corr()
sns.heatmap(corl,cmap="BrBG",annot=True)
print(corl)


### Ex_9
# Plotting a scatter plot
fig, ax = plt.subplots(figsize=(10,6))
ax.scatter(dataset[3], dataset[5])
ax.set_xlabel('Triceps skinfold thickness ')
ax.set_ylabel('Body mass index')
plt.show()