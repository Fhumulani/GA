import numpy as np
def mutate(child,Pm):
   child = list(child)[:]
   chil = ''
   for i in range(len(child)):
      #print(child[i])
      if np.random.random() < Pm:
        child[i] = int(not(bool(int(child[i]))))
 
      chil = chil+str(child[i])
   return chil
   
      
