import matplotlib.pyplot as plt
import numpy as np

# make data
plt.figure("demo")
x = np.linspace(-5, 5, 100)
y = x**2/4


plt.plot(x, y, linewidth=2.0)

plt.show()