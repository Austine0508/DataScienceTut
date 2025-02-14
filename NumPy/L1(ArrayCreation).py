import numpy as np

a1=np.array([1,2])# 1-d Array
print("1-d array:\n",a1,"\n")

a2=np.array([[1,2],[3,4]]) # 2-d Array
print("2-d array:\n",a2,"\n")

a3=np.array([[[1,2],[3,4]],[[5,6],[7,8]]]) # 3-d Array
print("3-d array:\n",a3,"\n")

a4=np.zeros((3,3)) # Zero Matrix
print("Zero Matrix:\n",a4,"\n")

a5=np.ones((2,2)) # Matrix with only 1
print("Ones Matric:\n",a5,"\n")

a6=np.arange(0,10,2) # 1-d grid of numbers from 0 to 10 with gap of 2
print("Range Matrix:\n",a6,"\n")
