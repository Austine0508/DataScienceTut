import numpy as np
a1=np.array([10,20,30])

print("1-d Indexing:")
print("Normal Indexing: ",a1[1]);
print("Negative Indexing: ",a1[-1]);

a2=np.array([[1,2,3],[4,5,6]])

print("\n2-d Indexing:");
print(a2[1,2]) # prints 2nd row 3rd element

print("\nSlicing:")
print("1-dimensional slicing: ",a2[1:4])
print("2-dimensional slicing: ",a2[:,1]) # prints second element of every row

print("\nAdvanced Indexing (uses conditions and other arrays)");
indices=np.array([0,1])
print(a1[indices])
cond=a1>0
print(a1[cond])

# negative indexing can also be used. Eg: -1 (accesses last element),-2 etc
