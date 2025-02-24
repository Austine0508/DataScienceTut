import numpy as np

a1=np.array([[1,2,3],[4,5,6]]) 
a2=np.array([[7,8,9],[10,11,12]]) 

h_arr=np.hstack((a1,a2))
print("Horizontal Stacking:\n",h_arr,"\n")

v_arr=np.vstack((a1,a2))
print("Vertical Stacking:\n",v_arr,"\n")

h_concat=np.concatenate((a2,a1),axis=1)
print("Concatenation Horizontal:\n",h_concat,"\n")

v_concat=np.concatenate((a2,a1),axis=0)
print("Concatenation Vertical:\n",v_concat,"\n")

# combining a 1-d and 2-d array is basically cross product
print("1-d 2-d combination:")
d1_arr=np.arange(5)
d2_arr=np.arange(10).reshape(2,5)

for a,b in np.nditer([d1_arr,d2_arr]):
    print(a,"-->",b)


