import numpy as np

class optimizer:
    def __init__(self, function, lb, ub, omega, phi_r, phi_g, swarm_size = 100,
            max_iterations = 100, min_variation = 1e-8, debug = False):
        self.function = function
        self.lb = np.array(lb)
        self.ub = np.array(ub)
        self.omega = omega
        self.phi_r = phi_r
        self.phi_g = phi_g
        self.size = swarm_size
        self.iterations = max_iterations
        self.minv = min_variation
        self.debug = debug
        self.init_swarm()

    def init_swarm(self):
        D = len(self.lb)
        self.D = D
        S = self.size
        self.x = np.random.uniform( self.lb, self.ub, size = (S,D) )

        fx = self.function(self.x)
        i_min = np.argmin(fx)

        self.best_x = self.x[i_min,:].copy()
        self.best_fx = self.function(self.best_x)

        dv = np.abs(self.ub - self.lb)
        self.v = np.random.uniform( -dv, dv, size = (S,D))
        self.pbest = np.zeros_like(self.x)
        self.pbestfx = np.apply_along_axis(self.function, 1, self.x)

    def do_one_iteration(self):

        rp = np.random.uniform(0, 1, size = (self.size, self.D) )
        rg = np.random.uniform(0, 1, size = (self.size, self.D) )

        self.v = self.v * self.omega + rp * self.phi_r * ( self.pbest - self.x) + rg * self.phi_g * (self.best_x - self.x)
        self.x = self.x + self.v

        fx = np.apply_along_axis(self.function, 1, self.x)
        idx = np.logical_and((fx < self.pbestfx), fx)

        self.pbest[idx,:] = self.x[idx,:]
        self.pbestfx[idx] = fx[idx]

        i_min = np.argmin(fx)

        self.best_x = self.x[i_min,:].copy()
        self.best_fx = fx[i_min]

    def run(self):

        for i in range(0, self.iterations + 1):
            best= self.best_fx
            self.do_one_iteration()
            if self.debug:
                print "[+] Best particle in iteration %d: %s with value %f" %(i, self.best_x, self.best_fx)
            if np.abs( best - self.best_fx) < self.minv:
                print "[+] Stopping because no variation since last minimum"
                break;
        return self.best_x, self.best_fx
