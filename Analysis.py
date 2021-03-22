#import pandas
import pandas as pd

#load cancer data into dataframe
df = pd.read_csv('data.csv')

#display first five rows of data
df.head()

#print the column labels in the dataframe
for i, v in enumerate(df.columns):
    print(i, v)

#this returns a tuple of the dimensions of the dataframe
df.shape

#this returns the datatypes of the columns
df.dtypes

# although the datatype for diagnosis appears to be object, further
# investigation shows it's a string
type(df['diagnosis'][0])

# this displays a concise summary of the dataframe,
# including the number of non-null values in each column
df.info()

# this returns the number of unique values in each column
df.nunique()

# this returns useful descriptive statistics for each column of data
df.describe()

# this returns the first few lines in our dataframe
# by default, it returns the first five
df.head()

# although, you can specify however many rows you'd like returned
df.head(20)

# same thing applies to `.tail()` which returns the last few rows
df.tail(2)

# View the index number and label for each column
for i, v in enumerate(df.columns):
        print(i, v)

# select all the columns from 'id' to the last mean column
df_means = df.loc[:,'id':'fractal_dimension_mean']
df_means.head()

# repeat the step above using index numbers
df_means = df.iloc[:,:12]
df_means.head()

# import
import numpy as np

# create the standard errors dataframe
indexes = np.r_[0:2, 12:22]
df_se = df.iloc[:, indexes]

# view the first few rows to confirm this was successful
df_se.head()

##CLEANING PRACTICE
# import pandas and load cancer data
import pandas as pd
df_means = pd.read_csv('cancer_data_means.csv')

# check which columns have missing values with info()
df_means.info()

# use means to fill in missing values
mean = df_means['texture_mean'].mean()
df_means['texture_mean'] = df_means['texture_mean'].fillna(mean)

mean = df_means['smoothness_mean'].mean()
df_means['smoothness_mean'] = df_means['smoothness_mean'].fillna(mean)

mean = df_means['symmetry_mean'].mean()
df_means['symmetry_mean'] = df_means['symmetry_mean'].fillna(mean)
# confirm your correction with info()
df_means.info()

# check for duplicates in the data
df_means.nunique()

# check for duplicates in the data
sum(df_means.duplicated())

# drop duplicates
df_means.drop_duplicates(inplace=True)

# confirm correction by rechecking for duplicates in the data
sum(df_means.duplicated())

# remove "_mean" from column names
new_labels = []
for col in df_means.columns:
    if '_mean' in col:
        new_labels.append(col[:-5])  # exclude last 6 characters
    else:
        new_labels.append(col)

# new labels for our columns
new_labels

# assign new labels to columns in dataframe
df_means.columns = new_labels

# display first few rows of dataframe to confirm changes
df_means.head()

# save this for later
df_means.to_csv('cancer_data_edited.csv', index=False)
