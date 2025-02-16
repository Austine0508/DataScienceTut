import numpy as np

dtypes=[('name','S10'),('grad_yr',int),('cgpa',float)] # Table Headings. 'S10' signifies string type with length 10 characters
values=[('Delno',2027,7.0),('Austine',2027,8.5),('Elvin',2028,6.6)] # Table Values
arr=np.array(values,dtype=dtypes) # Table Creation

print("Table:\n",arr)

print("\nSorting by Name:\n",np.sort(arr,order='name')) # Sorting by Name

print("\nSorting by Grad Yr and CGPA: \n",np.sort(arr,order=['grad_yr','cgpa'])) # Sorting by Grad Yr and CGPA
