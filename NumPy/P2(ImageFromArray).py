import numpy as np
from PIL import Image as im

# There are 1024*720=737280 pixels. arange them in a line first
arr=np.arange(737280,dtype=np.uint8)
print("1\n",arr)

# Resize the array to form a matrix that can be converted into greyscale image
# Therefore, reshape to 1024x720
arr=np.reshape(arr,(1024,720))
print("2\n",arr)

data=im.fromarray(arr)
# Above line convert arrays into PIL objects

data.save('mypic.png')
# Above line saves PIL objects in desired format
