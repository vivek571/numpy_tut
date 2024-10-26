import numpy as np

a=np.arange(1,20)
print(a)

a=np.arange(1,20,2)
print(a)

a=np.arange(2,20,2)
print(a)
print(type(a))

a=a.reshape((3,3))
print(a)

a=a.reshape((9,))
print(a)

b=np.arange(1,100,2)
print(b)

b=b.reshape(10,5)
print(b)

b=b.flatten()
print(b)

#Flatten and ravel
a=np.array([(1,2,3,4), (3,1,4,2)])
print(a)
print(a.shape)
c=a.flatten()
print("Flatten Array: ",c)
print("Original Array: ",a)


ra=np.ravel(a)
print("Flatten Array using ravel: ",ra)
ra[3]=44
print("Original Array: ",a)