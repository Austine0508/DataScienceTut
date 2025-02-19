import numpy as np

def gaussian_filter(kernel_size,sigma=1,muu=0): # sigma is standard deviation and muu is mean 
    x=np.linspace(-2,2,kernel_size)
    y=np.linspace(-2,2,kernel_size)

    X,Y=np.meshgrid(x,y)

    normal=1/(2*np.pi*sigma**2)

    dst=(X**2+Y**2)/(2*sigma**2)

    gauss=normal*np.exp(-1*dst) 

    print(gauss)

while (True):
    kernel_size=int(input("Enter Kernel Size (Enter 0 to Exit): "))
    if (kernel_size==0):
        break
    gaussian_filter(kernel_size)
    

