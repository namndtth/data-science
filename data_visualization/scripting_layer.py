import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(10000)
plt.hist(x, 1000)
plt.title(r'Normal distribution with $\mu=0, \sigma=1$')
plt.show()