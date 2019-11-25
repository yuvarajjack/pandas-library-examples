from pandas import *
import os
#print(os.listdir(os.getcwd())
data = read_csv('20190928-reviews.csv')
print("+-"*70)

#to print colums !
print("printing columns...\n")
col = data.columns
print(col)

print("+-"*70)
#to rewrite columns use rename
print("Renaming Data \"helpfullVotes\" with \"helpfulvotes\"  \n" )
data.rename(columns = {'helpfulVotes': 'helpfulvotes'}, inplace = True)
print("Rewrited Columns : ",data.columns)
print("+-"*70)

#To print the empty data, use isnull(), it will return empty data
print("Printing Data Framne \n",data.isnull())
print("+-"*70)

#to find how many data cells are empty, use sum()
print("Printing total missing values :\n",data.isnull().sum())

#Now lets remove null valuse use dropna(), it drops null columns by using axis
print(data.dropna(axis = 1))


