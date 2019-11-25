from pandas import *
import os
#print(os.listdir(os.getcwd())
data = read_csv('20190928-reviews.csv', index_col = 'name')
print("+-"*70)

#lets extract a column and put it into a variable
votes = data['helpfulVotes']

print("Printing type of the variable :",type(votes))
print("+-"*70)
#To put data in data frame we need more than one columns

ratings = data[['title','rating']]
print("printing type of ratings :", type(ratings))
print("\nPrinting Data Frames \n",ratings.head())
