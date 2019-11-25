from pandas import *
import os
#print(os.listdir(os.getcwd())
data = read_csv('20190928-reviews.csv')
print("+-"*70)

#Lets take a column as Variable
helpful_votes = data['helpfulVotes']
#it Prints first 5 values in the column !
print("Printing first 5 Values ! \n")
print(helpful_votes.head())
print("+-"*70)
#to find average or mean. use mean()
print("Printing Average of Votes \n")
average_vote = helpful_votes.mean().round()
print("Average Is :", average_vote)
print("+-"*70)

#To replace null values with average ! use "fillna()" and inplace overwrites the original columns

helpful_votes.fillna(average_vote, inplace = True)

print("Printing Overwrited data\n",data.isnull().sum())
print("+-"*70)

#Describe() is used to get detailed info about entire data
print(data.describe())
print("+-"*70)

#We can describe specific column tooo like thi
print("Printing Detail about title column!\n")
print(data['title'].describe())
print("+-"*70)

#to print specific data
print("printing top")
print(data['title'].value_counts().head(10))
print("+-"*70)
#we can print relation between data by corr()
print("Printing Relation \n",data.corr())
