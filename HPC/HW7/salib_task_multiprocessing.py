from SALib.sample import saltelli
from SALib.analyze import sobol
from SALib.test_functions import Ishigami
import numpy as np
from math import *
import time
from numba import njit
from multiprocessing import Process, Manager


a = 0.1
b = 0.5
c = 0.2

@njit
def evaluate_model(x, proc_num, return_dict):
    # s = 0
    # for i in range(1000):
    #    s += i * x[i % 2]
    retrun_dict[proc_num] = proc_num
    return a * x[2] * cos(x[0]) + b * sin(x[1]) * sin(x[1]) * sin(x[2]) + c * sin(x[0]) * x[2] ** 2 

problem = {
  'num_vars': 3,
  'names': ['x1', 'x2', 'x3'],
  'bounds': [[-np.pi, np.pi]]*3
}

# Generate samples
n = 2 ** 10
start = time.time()
param_values = saltelli.sample(problem, n)
print("Generation took %s seconds:" %(time.time() - start))

print(param_values)
if __name__ == '__main__':
    # Run model (example)
    Y = np.zeros([param_values.shape[0]])

    start = time.time()
    manager = Manager()
    return_dict = manager.dict()
    return_dict = []
    jobs = []
    for i, X in enumerate(param_values):
        p = Process(target=evaluate_model, args=(X, i, return_dict))
        jobs.append(p)
        p.start()

    for job in jobs:
        job.join()
    Y = np.array(return_dict.values())
    # Y = np.array(return_dict)

    print("Evaluation took %s seconds:" %(time.time() - start))

    start = time.time()
    Si = sobol.analyze(problem, Y)

    print("SA took %s seconds:" %(time.time() - start))
    print("First order")
    print(Si['S1']) # first order
    print("Total")
    print(Si['ST']) # total
    # second order
    print("Second order")
    print("x1-x2", Si['S2'][0,1])
    print("x1-x3", Si['S2'][0,2])
    print("x2-x3", Si['S2'][1,2])


