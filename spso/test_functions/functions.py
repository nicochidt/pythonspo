import numpy as np

# Let's define some test functions
def rastrigin(x):
    # https://en.wikipedia.org/wiki/Rastrigin_function
    # Minimum is  f(0,0,...,0) = 0
    # search space: 5.12 < x < 5.12
    A = 10
    return  A * x.shape[0] + np.sum( x**2 - A * np.cos(2 * np.pi * x))

def sphere(x):
    # Minimum at f(0,...,0) = 0
    # search space: -inf < x < inf
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
    # search space -5 < x < 5
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

def beale(x):
    # https://en.wikipedia.org/wiki/Test_functions_for_optimization
    # min f(3, 0.5) = 0
    # search space -4.5 < x,y < 4.5
    y = x[1]
    x = x[0]
    return (1.5 - x + x*y) ** 2 + (2.25 -x + x*(y**2)) ** 2 + (2.625 - x + x* (y**3) ) ** 2

def thcf(x):
    # three hump camel function
    # https://en.wikipedia.org/wiki/Test_functions_for_optimization
    # min f(0,0) = 0
    # search space -5 < x,y < 5
    y = x[1]
    x = x[0]
    return 2 * x**2 - 1.05 * x **4 + x **6 / 6. + x*y + y**2

functions = {
        'rastrigin': {
            'f': rastrigin,
            'lb': [-5.12, -5.12],
            'ub': [5.12, 5.12],
            'min': [0,0],
            'fmin': 0
            },
        'sphere': {
            'f': sphere,
            'lb': [-1000, -1000],
            'ub': [1000, 1000],
            'min': [0,0],
            'fmin': 0
            },
        'ackley': {
            'f': ackley,
            'lb': [ -5, -5],
            'ub': [ 5, 5],
            'min': [ 0, 0],
            'fmin': 0
            },
        'eggholder': {
            'f': eggholder,
            'lb': [-512, -512],
            'ub': [512, 512],
            'min': [512, 404.2319],
            'fmin': -959.6407
            },
        'crossintray': {
            'f': crossintray,
            'lb': [-10, -10],
            'ub': [10,10],
            'min': [(1.34941,1.34941), (-1.34941,1.34941), (1.34941,-1.34941), (-1.34941,-1.34941)],
            'fmin': [ -2.06261, -2.06261, -2.06261, -2.06261]
            },
        'beale': {
            'f': beale,
            'lb': [-4.5, -4.5],
            'ub': [4.5, 4.5],
            'min': [ 3, 0.5 ],
            'fmin': 0
            },
        'three-hump-cf': {
            'f': thcf,
            'lb': [ -5, -5],
            'ub': [5, 5],
            'min': [0,0],
            'fmin': 0
            }
        }
