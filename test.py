import spo
import numpy as np

SWARM_SIZE = 100
ITERATIONS = 100

# Let's define some test functions
def rastrigin(x):
    # https://en.wikipedia.org/wiki/Rastrigin_function
    # Minimum is  f(0,0,...,0) = 0
    A = 10
    return  A * x.shape[0] + np.sum( x**2 - A * np.cos(2 * np.pi * x))

def sphere(x):
    # Minimum at f(0,...,0) = 0
    return np.sum(x**2)

def rosenbrock(x):
    # https://en.wikipedia.org/wiki/Rosenbrock_function
    # min is  f(a, a**2) = 0
    a,b = 2, 100
    y = x[1]
    x = x[0]
    return (a - x) ** 2 + b * ( y - x ** 2) **2

def ackley(x):
    # https://en.wikipedia.org/wiki/Ackley_function
    # min is f(0,0) = 0
    return -20 * np.exp( -0.2 * np.sqrt( 0.5 * np.sum(x**2))) - np.exp( 0.5 * np.sum(np.cos(2*np.pi*x))) + np.e + 20

def eggholder(x):
    # https://en.wikipedia.org/wiki/Test_functions_for_optimization
    # min is f(512, 404.2319) = -959.6407
    # search space: -512 <x,y< 512
    y = x[1]
    x = x[0]
    return - ( y + 47 ) * np.sin(np.sqrt(np.abs( 0.5 * x + y + 47 ) )) - x * np.sin(np.sqrt(np.abs( x - y - 47)))

def crossintray(x):
    # https://en.wikipedia.org/wiki/Test_functions_for_optimization
    # 4 mins:
    # a = 1.34941 f(a,a) = f(-a,a) = f(a,-a) = f(-a,-a) = -2.06261
    # search space: -10 < x,y < 10
    y = x[1]
    x = x[0]
    return -0.0001 * (np.abs(np.sin(x) * np.sin(y) * np.exp(np.abs(100 - np.sqrt(x**2 + y **2) / np.pi))) + 1 ) ** 0.1

args = {
        'swarm_size': SWARM_SIZE,
        'max_iterations': ITERATIONS,
        'function': ackley,
        'lb': [ -10,-10],  # lower bond for search space
        'ub': [10,10],     # upper bond for search space
        'omega': 0.5,
        'phi_r': 0.5,
        'phi_g': 0.5,
        'debug': False   # if True best position and value of each iteration is printed
     }

opt = spo.optimizer(**args)
x, fx = opt.run()
print "[+] Algorithm returned %s with value %f" % ( x, fx)

