import pandas as pd

# read the data in 'bank.csv' into python
df = pd.read_csv('bank.csv')
print(df)

# Find the maximum balance in the bank data
print(df['balance'].max())

## Print Print the job and age of the person who has the maximum balance
# print job and age separately
print(df['age'][df['balance'] == df['balance'].max()])
print(df['job'][df['balance'] == df['balance'].max()])

# print job and age together         
print(df[['age','job']][df['balance'] == df['balance'].max()])
