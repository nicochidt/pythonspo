import spo
from test_functions.functions import *
import numpy as np

SWARM_SIZE = 200
ITERATIONS = 100


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

for k,v in functions.iteritems():

    args = {
        'swarm_size': SWARM_SIZE,
        'max_iterations': ITERATIONS,
        'function': v['f'],
        'lb': v['lb'],   # lower bond for search space
        'ub': v['ub'],     # upper bond for search space
        'omega': 0.5,
        'phi_r': 0.5,
        'phi_g': 0.5,
        'debug': False   # if True best position and value of each iteration is printed
     }
    print "[+] Optimizing function %s" % k
    opt = spo.optimizer(**args)
    x, fx = opt.run()
    print "[+] Algorithm returned %s with value %f" % ( x, fx)
    print "[+] Function minimum is at %s with value %s" % (v['min'], v['fmin'])
    print "\n"

