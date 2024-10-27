import numpy as np

a=np.arange(0,18).reshape(6,3)
print(a)
b=np.arange(20,38).reshape(6,3)
print(b)

# print(a*b)
# print(a+b)
# print(a-b)
# print(a/b)
print(a.shape)
print(b.shape)

b=b.reshape(3,6)
print(a.shape)
print(b.shape)
print(a@b)