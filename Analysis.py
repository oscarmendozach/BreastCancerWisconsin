#import pandas
import pandas as pd

#load cancer data into dataframe
df = pd.read_csv('data.csv')

#display first five rows of data
df.head()

#print the column labels in the dataframe
for i, v in enumerate(df.columns):
    print(i, v)
