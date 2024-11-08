import numpy as np
import matplotlib.pyplot as plt

xx = np.linspace(1, 50, 1001)
yy = np.sin(xx * np.log(np.sqrt(xx)))

plt.plot(xx, yy, 'o')
plt.show()
