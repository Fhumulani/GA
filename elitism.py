import numpy as np
import pandas as pd
def ellist(pop,Er):
    M = len(pop)
    Elit_no = int(round(M*Er))
    fitness1 = pop.fitness
   
    ww = pop.sort_values(['fitness'],ascending=False)
    
    sorted_idx= list(pop.index)    
    nom_fit = list(pop.fitness)
    
    newpopulation = np.array(pop.drop(['fitness'],axis=1))
    fitness = []
    for i in range(Elit_no+1):
        newpopulation[i] = ww.genes.iloc[sorted_idx[i]][:]
        fitness.append(nom_fit[i])
   
    for i in range(Elit_no+1,M):
        newpopulation[i] = pop.genes.iloc[i][:]
        fitness.append(fitness1[i])
    newpopulation = pd.DataFrame(newpopulation,columns=['genes'])
    newpopulation['fitness'] = fitness

    return newpopulation

