import numpy as np 

"""
get the annotation for the yolo's type.
x_1,y_1 is upper letf point
w and h is weight and height
W_ and H_ is pixel's Weight and Height.
xcen = ((x_1+w/2)/W_)
ycen = ((y_1+h/2)/H_)
w_ = w/W_
h_ = h/H_
"""
bb =np.loadtxt('bb.txt',dtype=str)
pixel = np.loadtxt('pixel.txt',dtype=str) 
print(bb.dtype, pixel.dtype)
# a = float(bb[:,1])*float(bb[:,2])
bb1 = bb[:,1:].astype(float)
pixel1 = pixel[:,1:].astype(float)
x_1 = bb1[:,0]
y_1 = bb1[:,1]
w   = bb1[:,2]
h   = bb1[:,3]
W_  = pixel1[:,0]
H_  = pixel1[:,1]
xcen = ((x_1+w/2)/W_)
ycen = ((y_1+h/2)/H_)
w_ = w/W_
h_ = h/H_
zzz = np.empty((202599,))
#print(zzz.shape,x_1.shape,y_1.shape,w_.shape,h_.shape)
L = np.vstack((zzz,xcen,ycen,w_,h_))
#np.savetxt('nnn11.txt',L.T,fmt='%3f')
np.savetxt('nnn12.txt',L.T,fmt='%i %3f %3f %3f %3f') 
"""
first col's dtype is int , the others dtype is %3f
"""
print(L.shape)
