import numpy as np
import matplotlib.pyplot as plt

xx = np.arange(-10, 50, 50)
xx2 = np.arange(-10, 50, .1)

plt.plot(xx, np.sin(xx))
plt.plot(xx2, np.sin(xx2))
#plt.plot(xx, np.sqrt(xx))
plt.show()
