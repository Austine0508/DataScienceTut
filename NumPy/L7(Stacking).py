import numpy as np

a1=np.array([[1,2,3],[4,5,6]]) 
a2=np.array([[7,8,9],[10,11,12]]) 

h_arr=np.hstack((a1,a2))
print("Horizontal Stacking:\n",h_arr)

v_arr=np.vstack((a1,a2))
print("Vertical Stacking:\n",v_arr)
