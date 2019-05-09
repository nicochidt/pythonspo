import spso
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.lines import Line2D
plt.style.use('ggplot')

# this module contains several functions to test optimizers
from test_functions import functions


args = {
            'function': functions.beale,
            'lb': [-10, -10],
            'ub': [10, 10],
            'history': True
        }

opt = spso.optimizer(**args)
x, fx = opt.run()
history = opt.get_history()

fig, ax = plt.subplots(nrows = 1)
def create_image(x, y, values, p):
    ax.clear()
    ax.contour(x, y, values, linewidths = 0.3)
    k = ax.scatter(p[0], p[1], marker = '+')
    return k,

x = np.linspace( args['lb'][0], args['ub'][0], 100)
y = np.linspace( args['lb'][1], args['ub'][1], 100)
mesh = np.meshgrid(x,y)
values = args['function'](mesh)

imgs = []
for i in range(1, len(history)):
    imgs.append(create_image(x, y, values, history[i]))

gif = animation.ArtistAnimation(fig, imgs, interval=300, blit=True, repeat_delay=1000)

plt.show()


