import numpy as np
import matplotlib.pyplot as plt

xx = np.linspace(-10, 10, 1001)

xx * (xx < 0)

def f(x):
    if x < 0:
        return np.sin(x)
    else:
        return np.sqrt(x)

yy = [f(x) for x in xx]

plt.plot(xx, yy)
plt.show()
