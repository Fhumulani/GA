import numpy as np
import pandas as pd
def initialize(M,N):
   pops = pd.DataFrame()
   population = np.zeros((M,N))
   for i in range(M):
       popu = ''
       for j in range(N):
          population[i][j] = np.random.randint(0,2)
          popu = popu+str(int(population[i][j]))
       pops= pops.append([popu],ignore_index=True)
   pops.columns = ['genes']
   return pops
