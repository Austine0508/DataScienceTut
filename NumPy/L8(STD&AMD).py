import numpy as np

a=np.array([1,2,3,8,9,10])

# Calculate AMD (Absolute Mean Deviation)
print("Array: ",a)
d=np.mean(a) # this is the mean of data
print("Mean: ",d)
deviation=a-d
print("Deviation: ",deviation)
abs_deviation=abs(deviation)
print("Absolute Deviation: ",abs_deviation)
amd=np.sum(abs_deviation)/len(a)
print("\nAbsolute Mean Deviation: ",amd)

# Calculate STD (Standard Deviation)
print("\nStandard Deviation: ",np.std(a))
