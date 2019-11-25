from pandas import *
import os
#print(os.listdir(os.getcwd())
data = read_csv('20190928-reviews.csv', index_col = 'name')
print("+-"*70)

print(data.columns)
print("+-"*70)
#to print rating 5, if its 5 it will return True
print(data['helpfulVotes'] == 5)
print("+-"*70)

#to print this into dataframes
vote =data[data['helpfulVotes'] == 5 ]
print("Printing in DataFrame :")
print(vote.head(10))
print("+-"*70)
#lets filter which is lower than 5
print("Printing first three data which have lesser than rating 5: ")
print(data[data['helpfulVotes'] <= 5].head(3))
