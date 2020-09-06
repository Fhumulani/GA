import GeneAlg as ga
import warnings
warnings.filterwarnings("ignore")
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import time

import Sphere

M = 20 #number of chromoseomes

N = 20 #number of genes

MaxGen = 2;
Pc = 0.85;
Pm = 0.01;
Er = 0.05;
now = time.time()
fit = ga.GA(M,N,MaxGen,Pc,Pm,Er,Sphere,'double')
print(time.time()-now)
plt.plot(range(MaxGen),fit,"-o")
plt.xlabel("Generation no#")
plt.ylabel("fitness")
plt.savefig("GA.png")
#plt.show()



   
