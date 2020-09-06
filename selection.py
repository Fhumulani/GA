import numpy as np
import pandas as pd
import time
def selection(population):
    #nom_sum = sum(population['fitness'])
    normalized_fitnesses = population['fitness']/sum(population['fitness'])
    
    
    
    nom = normalized_fitnesses.sort_values(ascending=False)
    
    sorted_idx= list(nom.index)
    
    nom_fit = list(nom[:])

    
    temp_pop = np.array(population.drop(['fitness'],axis=1))
    
    fitness = []
    #now = time.time()
    for i in range(len(population)):        
        temp_pop[i] = population.genes.iloc[sorted_idx[i]][:]
        fitness.append(nom_fit[i])
    #print(time.time()-now)
    temp_pop = pd.DataFrame(temp_pop,columns=['genes'])
    temp_pop['fitness']=fitness
    
    
	
      
    #cumsums = np.zeros((len(population),1))
    cumsums = list([0]*len(population))


    for i in range(len(cumsums)):        
        cumsums[i] = sum(temp_pop.fitness[i:])

    R = np.random.random()
    parent1_idx = len(population)-1;
    for i in range(0,len(cumsums)):
        if R > cumsums[i]:
            parent1_idx = i-1;
            break;

    parent2_idx = parent1_idx;

    while parent2_idx == parent1_idx:
        R = np.random.random()
        for i in range(0,len(cumsums)):
            if R > cumsums[i]:
                parent2_idx = i-1;
                break;

    return temp_pop.genes[parent1_idx],temp_pop.genes[parent2_idx]
