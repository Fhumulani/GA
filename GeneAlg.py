import numpy as np
import innit 
import pandas as pd
import crossover as cs
import mutation as mt
import matplotlib.pyplot as plt
import selection as sel
import elitism as el
import time

def GA(M,N,MaxGen,Pc,Pm,Er,bb,method):

    population = innit.initialize(M,N)



    fitness = []

    for i in range(M):
       fitness.append(bb.fitnes(population.genes[i]))

    population['fitness'] = fitness
    

    newpop = np.array(population.drop(['fitness'],axis=1))
    print("generation  #{0}".format(1))
    
    fitnesses = [0]
    for i in range(1,MaxGen): 
       print("generation  #{0}".format(i+1))
       
       for j in range(0,M,2):
           
	  
          p1, p2 = sel.selection(population)
          
         
          
          chilld1,chilld2 = cs.cross(p1,p2,Pc,method)

          
          child1 = mt.mutate(chilld1,Pm)
          child2 = mt.mutate(chilld2,Pm)
	  
          
       
          newpop[j] = child1
    
          newpop[j+1] = child2
       newpopulation = pd.DataFrame(newpop,columns=['genes'])
	  
       fitness1 = []
       for i in range(M):
           fitness1.append(bb.fitnes(newpopulation.genes[i]))
       newpopulation['fitness'] = fitness1
       
       
       newpopulation = el.ellist(newpopulation, Er)
       
       
       population = newpopulation.copy();
       newpopulation.sort_values(['fitness'],inplace=True,ascending=False)
       newpopulation= newpopulation.reset_index(drop=True)
         
       maxx = max(newpopulation.fitness)
       #print(maxx) 
       #print(maxx,newpopulation.genes[newpopulation.fitness == maxx].iloc[0])
       fitnesses.append(maxx)
    return fitnesses

    #fitness2 = []
    #for i in range(M):
     #      fitness2.append(bb.fitnes(newpopulation.genes[i]))
    #newpopulation['fitness'] = fitness2
    


