#####
# Lab8: Task 1
#####

import pandas as pd

df = pd.read_csv("iris.csv")
print(df.shape)

print(df.head(5))

# Checking the types of data
print(df.dtypes)

# Checking rows containing duplicate data
duplicate_rows_df = df[df.duplicated()]
print("number of duplicate rows: ", duplicate_rows_df.shape)

# Dropping the duplicates 
df = df.drop_duplicates()
# Counting the number of rows after removing duplicates.
df.count()

# Count the number of null values in each column
print(df.isnull().sum())

# Printing summary statistics on attributes
print(df.describe())


### Plot the histograms

# import libraries
import seaborn as sns
import matplotlib.pyplot as plt

# set a grey background (use sns.set_theme() if seaborn version 0.11.0 or above) 
sns.set(style="darkgrid")

fig, axs = plt.subplots(2, 2, figsize=(8, 8))

sns.histplot(data=df, x="sepal length", kde=True, color="gold", ax=axs[0, 0])
sns.histplot(data=df, x="sepal width", kde=True, color="skyblue", ax=axs[0, 1])
sns.histplot(data=df, x="petal length", kde=True, color="teal", ax=axs[1, 0])
sns.histplot(data=df, x="petal width", kde=True, color="olive", ax=axs[1, 1])

plt.show()

#create a dataframe with all variables except the class column
X = df.drop(['class'], axis=1)

#check that the class variable has been removed
X.head()

"""
# Scaling the variables into the range [0,1] 
from sklearn.preprocessing import MinMaxScaler

# define min max scaler
scaler = MinMaxScaler()
# transform data
X = scaler.fit_transform(X)

#check the scaled X
print(X[0:5])
"""

#separate target values
y = df["class"].values

#view target values
print(y[0:5])

# using the 'train_test_split' function from sklearn to split the dataset
from sklearn.model_selection import train_test_split

X_train, X_Vali_test, y_train, y_Vali_test = train_test_split(X, y, test_size=0.2, 
                                                    random_state=1, stratify=y)

print(X_train.shape)



from sklearn.neighbors import KNeighborsClassifier

# Create KNN classifier
knn = KNeighborsClassifier(n_neighbors = 3)

# Fit the classifier to the data
knn.fit(X_train,y_train)

#show first 5 model predictions on the test data
print(knn.predict(X_Vali_test)[0:5])

#check accuracy of our model on the test data
knn.score(X_Vali_test, y_Vali_test)

