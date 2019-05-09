Simple swarm particle optimizer 

Ussage: 

```python
import pso
import numpy as np 

def example_function(x): 
    return np.sum(x**2)

lb = [ -5, -5, -5] # lower bound of search space 
ub = [ 5, 5, 5]    # upper bound of search space

opt = pso.optimizer( example_function, lb, ub)
x, fx = opt.run()
```

Other values of the algorithm can be specified: 

```python
args = {
         'swarm_size': 50,
         'max_iterations': 100,
         'function': example_function,
         'lb': [ -10,-10],  
         'ub': [10,10],     
         'omega': 0.5,
         'phi_r': 0.5,
         'phi_g': 0.5,
         'debug': False   
      }
opt = pso.optimizer(**args)
x,fx = opt.run()
```


