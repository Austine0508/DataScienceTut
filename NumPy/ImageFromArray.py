import numpy as np
from PIL import Image as im

arr=np.arange(737280,dtype=np.uint8)
print("1\n",arr)
arr=np.reshape(arr,(1024,720))
print("2\n",arr)
data=im.fromarray(arr)
data.save('mypic.png')
