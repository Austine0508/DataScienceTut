import numpy as np

# Vectors are 1-D arrays
# They can be Horizontal or Verticcal

v1=np.array([1,2,3]) # Horizontal Vector
v2=np.array([[1],[2],[3]]) # Vertical Vector

print("Horizontal Vector: \n",v1)
print("\nVertical Vector: \n",v2)

# All basic operations can be performed on vertors (add, subtract, multiply, divide)

# dot product can also be accomplished

print("\nDot Product: ",v1.dot(v2))

# scalar product can also be obtained

print("\n Scalar Product: \n",v1*5,"\n\n",v2*5)
