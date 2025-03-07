import cv2
import numpy as np

array=np.zeros([500,500,3],dtype=np.uint8) # Creates an array with 500 matrices of 500 rows and 3 columns with 0 as values
# In our work here, above line indicates, 500x500 pixels and 3 refers to the color channel RGB (red, green, blue -3)
# dtype is optional. It specifies the type of data

array[:,:]=[255,255,255] # This lines changes all values to 255
# 255,255,255 is rgb value of white

cv2.imshow("image",array) # Prints our white image
# "image" is name of window
