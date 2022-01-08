# Importing required libraries.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt #visualisation
import seaborn as sns #visualisation

sns.set(color_codes=True)

# The following line is needed to set backend of matplotlib to inline
# to view visuals in Jupyter Notebook.
# Comment it out if you are using Spyder or Google Colab
%matplotlib inline 



# Load the data into Pandas dataframe and check the number of rows and columns
df = pd.read_csv("cardata.csv")
print df.shape


# To display the top 5 rows
df.head(5)


# To display the bottom 10 rows
df.tail(10) 


# Checking the data type
print df.dtypes


# Rows containing duplicate data
duplicate_rows_df = df[df.duplicated()]
print "number of duplicate rows: ", duplicate_rows_df.shape


# Dropping the duplicates 
df = df.drop_duplicates()

# Counting the number of rows after removing duplicates.
df.count()


# Count the number of null values in each column
print(df.isnull().sum())


# Dropping the missing values.
df = df.dropna() 
print df.count()
print df.shape


# Printing summary statistics on attributes
print df.describe()


# Plotting a bar chart for make variable
df.Make.value_counts().nlargest(40).plot(kind='bar', figsize=(10,5))
plt.title("Number of cars by make")
plt.ylabel('Number of cars')
plt.xlabel('Make');


# plot the histogram of Engine HP
plt.hist(df['Engine HP'], bins=20)
plt.title("Histogram of Engine HP")
plt.ylabel('Number of Engine HP')
plt.xlabel('Value of Engine HP');



# Finding the relations between the variables.
plt.figure(figsize=(20,10))
corl= df.corr()
sns.heatmap(corl,cmap="BrBG",annot=True)
print corl



# Plotting a scatter plot
fig, ax = plt.subplots(figsize=(10,6))
ax.scatter(df['Engine HP'], df['Price'])
ax.set_xlabel('Engine HP')
ax.set_ylabel('Price')
plt.show()

