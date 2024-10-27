import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')

print(np.pi)
print(np.sin(np.pi/2))

x=np.arange(1,11)
y=np.arange(10,110,10)

plt.figure(figsize=(4,4))
plt.plot(x,y,'r--')
plt.show()