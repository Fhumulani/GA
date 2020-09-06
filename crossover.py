import numpy as np
def cross(p1,p2,Pc,crossName):
    
    if crossName == 'single':
        lb = 1
        ub = len(p1)-1
        crossP = int(round((ub-lb)*np.random.random()+lb))
        child1 = p1[:crossP]+p2[crossP:]
        child2 = p2[:crossP]+p1[crossP:]
	
    if crossName == 'double':
        lb = 1
        ub = len(p1)-1
        crossP1 = int(round((ub-lb)/2*np.random.random()+lb))
        crossP2 = crossP1 + int(round((ub-lb)/2*np.random.random()+lb))
        child1 = p1[:crossP1]+p2[crossP1:crossP2]+p1[crossP2:]
        child2 = p2[:crossP1]+p1[crossP1:crossP2]+p2[crossP2:]
	
    R1 = np.random.random()

    if R1 > Pc:
        child1 = p1

    R2 = np.random.random()

    if R2 > Pc:
         child2 = p2

    return child1,child2
