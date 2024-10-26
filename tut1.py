import numpy as np

lst = [1,2,3,4,5]
print(lst)

print("1D Array")
a = np.array([1,2,3,4,5])
print(a)

print("2D Array")
b = np.array([
    [1,2,3,4,5],
    [11,12,13,14,15]
     ])
print(b)

print("3D Array")
c=np.array([[
    [1,2,3,4,5],
    [11,12,13,14,15],
    [21,22,23,24,25]
]])
print(c)
#Type of object
print(type(a))

#Size of ndarray
print(a.size)
print(b.size)
print(c.size)

#Shape of array
print(a.shape)
print(b.shape)
print(c.shape)

#Get data type
print(c.dtype)