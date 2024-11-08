import numpy as np
import matplotlib.pyplot as plt

xx = np.linspace(1, 2, 1001)

def f(x):
    return np.tan(x)

yy = [f(x) for x in xx]

plt.plot(xx, yy)
plt.show()
