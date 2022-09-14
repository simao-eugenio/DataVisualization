
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('tkAgg')
import numpy as np

t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2*np.pi*t)
plt.plot(t, s)

plt.title('About as simple as it gets, folks')
plt.show()

