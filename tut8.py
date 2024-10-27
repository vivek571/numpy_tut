import numpy as np
s1="Vivek is my name"
s2 = "I am India"
a=np.char.upper(s1)
a=s1+s2
a=np.char.lower(s1+s2)
a=np.char.split(s2)

s3="Vivek is my name    i am from\nindia"
# a=np.char.splitlines(s3)
a=np.char.replace(s3, 'name', 'n')
print(a)

print(np.char.center('Vivek Kumar Mishra', 120, '*'))

