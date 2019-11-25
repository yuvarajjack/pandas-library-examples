from pandas import *
import os
#print(os.listdir(os.getcwd())
data = read_csv('20190928-reviews.csv', index_col = "name")
print("+-"*70)

#it gives information about the data, datatype, size
print("Printing information about the data set......\n")
print(data.info())
print("+-"*70)
#it returns the shape of data in tuple. (rows,columns)
print("\nShape of Data is (rows,columns) :",data.shape)
print("+-"*70)
#prints first 10 data
print()

print("\nprinting first 10 data: \n",data.head())
print("+-"*70)

#doubling data to drop duplicates
temp = data.append(data)
print(temp.shape)

#to drop duplicate data use drop_duplicate
#keep takes three type of options... 
#first: (default) Drop duplicates except for the first occurrence.
#last: Drop duplicates except for the last occurrence.
#False: Drop all duplicates.

temp.drop_duplicates(inplace = True, keep = False)
print(temp.shape)
print(temp)
