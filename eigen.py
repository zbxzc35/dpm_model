from numpy import linalg as LA
from numpy.linalg import inv
import numpy as np
import itertools
import dpm

def get_eigen_decomposition(model, patient_data, M, I, J):
	#Get Qij
	interval = 10

	#Decomposition
	a, u = LA.eig(model.q)
	u_inv = inv(u)

	#Transition Pair
	seq=[]
	for i in xrange(M):
		seq.append(i)	
	combination = itertools.combinations(seq,2)
	
	#Calculate Qij	
	total_p = 0
	total_q_i = 0
	total_q_j = 0
	Akl = 0
	xpq = 0
	for patient in patient_data:
		for combi in combination:
			for p in xrange(M):
				total_p += u[combi[0]][p]*u_inv[I][J]
				for q in xrange(M):
					if p == q:
						xpq += interval*np.exp(interval*a[p])
					else:
						tmp = np.exp(interval*a[p])-np.exp(interval*a[q])
						xpq += tmp/(a[p]-a[q])
			for q_i in xrange(M):
				total_q_i += u[I][q_i]*u_inv[q_i][combi[1]]
			for q_j in xrange(M):
				total_q_j += u[J][q_j]*u_inv[q_j][combi[1]]
	
			Akl += model.get_transition_probability(combi[0], combi[1], interval)

	totalRi = xpq*total_p*total_q_i/Akl
	totalNi = xpq*model.get_transition_probability(I, J, 1)*total_p*total_q_j/Akl
	
	return totalRi, totalNi
