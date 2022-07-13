import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.set_title('График')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid()

x = np.linspace(0, 5, 100)
y = x
ax.plot(x, y)

plt.show()



















