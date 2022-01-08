#####
# Lab8: Task 3
#####


from pandas import read_csv
import matplotlib.pyplot as plt

# load the dataset
dataset = read_csv('insurance.csv', header=None)

# print the summary statistics on each attributes
print(dataset.describe())

# Rows containing duplicate data
duplicate_rows_df = df[df.duplicated()]
print("number of duplicate rows: ", duplicate_rows_df.shape)

# Commented out IPython magic to ensure Python compatibility.
# specify the input variable (x) and the target variable (y)
x = dataset[0]
y = dataset[1]

# plot the data
# the following line is not needed in Spyder
# %matplotlib inline
plt.scatter(x,y)

## Define the funcitons to be used in the coefficient calculation

# Calculate the mean value of a list of numbers
def mean(values):
    return sum(values) / float(len(values))

# Calculate the variance of a list of numbers
def variance(values, mean):
    return sum([(s - mean)**2 for s in values])

# Calculate covariance between x and y
def covariance(s, mean_s, t, mean_t):
    covar = 0.0
    for i in range(len(s)):
        covar += (s[i] - mean_s) * (t[i] - mean_t)
    return covar

# Function to calculate coefficients
def coefficients(in_var, target):
    x_mean, y_mean = mean(in_var), mean(target)
    b1 = covariance(in_var, x_mean, target, y_mean) / variance(in_var, x_mean)
    b0 = y_mean - b1 * x_mean
    return [b0, b1]

# estimate the best fitting regression line
b0, b1 = coefficients(x, y)

print('Coefficients: b0=%.3f, b1=%.3f' % (b0, b1))
print('The best regrssion line is: y = %.2f + %.2f * x' % (b0, b1))

# in irder to plot the regression line, calculate points on the line
x1 = range(130)
y1 = []
for i in x1:
    #x1.append(i)
    y1.append(b0 + b1*i)

# plot the regression line
plt.plot(x1,y1)
# plot the dataset in the same figure
plt.scatter(x,y)

# assuming in a new instance: the input variable is 85.72
x_k = 85.72

# predict the value of target varible using the regression model
y_k = b0 + b1 * x_k
print('the new instacnce is: %.2f, %.2f' % (x_k, y_k))

# plot the regression line and instances in the original dataset
plt.plot(x1,y1)
plt.scatter(x,y)

# plot the new instance in the figure as a triangle
plt.scatter(x_k, y_k, marker='^')


# === For question 9 ===
x01 = 46.12
x02 = 65.3

# predict the value of target variable using the regression model
y01 = b0 + b1 * x01
print('the new instacnce is: %.2f, %.2f' % (x01, y01))

y02 = b0 + b1 * x02
print('the new instacnce is: %.2f, %.2f' % (x02, y02))

