import spso
import numpy as np
import matplotlib.pyplot as plt

# this module contains several functions to test optimizers
from test_functions import functions

args = {
            'function': functions.crossintray,
            'lb': [-10, -10],
            'ub': [10, 10],
            'history': True
        }

opt = spso.optimizer(**args)
x, fx = opt.run()
history = opt.get_history()

x = np.linspace( args['lb'][0], args['ub'][0], 100)
y = np.linspace( args['lb'][1], args['ub'][1], 100)
mesh = np.meshgrid(x,y)
values = args['function'](mesh)

fig, ax = plt.subplots(nrows = 1)
ax.contour(x, y, values, linewidths = 0.3)
hx, hy = [], []
for p in history[:-1]:
    hx.append(p[0])
    hy.append(p[1])

ax.plot( hx, hy)
ax.scatter( history[-1][0], history[-1][1], marker = '+')
plt.show()


