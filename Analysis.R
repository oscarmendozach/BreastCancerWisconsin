#import dplyr
library(dplyr)

#load cancer data into dataframe

df <- read.csv(file = 'data.csv', 
               header = TRUE,
               sep = ",")

#display first five rows of data
head(df)

#print the column names
names(df)

