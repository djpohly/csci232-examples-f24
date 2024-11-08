import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)

X, Y = np.meshgrid(x, y)

def f(x, y):
    return -np.sin(np.sqrt(x**2 + y**2))

Z = f(X, Y)

# plt.plot(Z)
ax = plt.axes(projection="3d")
ax.contour3D(X, Y, Z, 100, cmap="seismic")

plt.show()
