import numpy as np

a=np.array([0,1,2,3]) # a,b,c are arrays undergoing operations
b=np.array([10,9,8,7])
c=np.array([-1,0,1])

print("Addition: \n")
print(a+b)
print("Similarly, subtraction, multiplication and division can be done")

print("\nUnary Operation: \n")
print(np.absolute(c))

print("\nBinary Operation: \n")
print(np.add(a,b))
