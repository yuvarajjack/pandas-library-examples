from pandas import *
import os
#print(os.listdir(os.getcwd())
data = read_csv('20190928-reviews.csv', index_col = 'name')
print("+-"*70)

#.loc - locates by name
#.iloc- locates by numerical index
names_1 = data.iloc[0]
print("Printing first row details >>>>>>>>>>>")
print(names_1)
print("+-"*70)

#if we want to slice roww we can do that by slicing strings in python [from:to]
print(data.iloc[0:11])

#lets filter by condition
