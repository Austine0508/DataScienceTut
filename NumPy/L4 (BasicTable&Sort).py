import numpy as np

dtypes=[('name','S10'),('grad_yr',int),('cgpa',float)]

values=[('Delno',2027,7.0),('Austine',2027,8.5),('Elvin',2028,6.6)]

arr=np.array(values,dtype=dtypes)

print("Table:\n",arr)

print("\nSorting by Name:\n",np.sort(arr,order='name'))

print("\nSorting by Grad Yr and CGPA: \n",np.sort(arr,order=['grad_yr','cgpa']))
