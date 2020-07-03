# Generate a histogram of 10,000 random numbers using artist layer

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas 
# agg stands for anti grain geometry

from matplotlib.figure import Figure

fig = Figure()
canvas = FigureCanvas(fig)

import numpy as np
x = np.random.randn(10000) 

ax = fig.add_subplot(111) # create an axes artist

ax.hist(x, 100) # generate a histogram of the 1000 numbers

ax.set_title('Normal distribution with $\mu=0, \sigma=1$')
fig.savefig('matplotlib_histogram.png')