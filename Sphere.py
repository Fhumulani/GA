import numpy as np
def fitnes(X):
    fitness_value = sum(np.square([(int(entry)) for entry in X]))
    return fitness_value
    
