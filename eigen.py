from numpy import linalg as LA
from numpy.linalg import inv
import numpy as np
import itertools

def get_eigen_decomposition(q, patient_data, M):
	#Get Qij
	interval = 10
	I=0
	J=0	

	#Decomposition
	a, u = LA.eig(q)
	u_inv = inv(u)

	xpq = interval*np.exp(interval*a)

	#Transition Pair
	seq=[]
	for i in xrange(M):
		seq.append(i)	
	combination = itertools.combinations(seq,2)
	
	#Calculate Qij	
	total_p = 0
	total_q_i = 0
	total_q_j = 0
	totalRi = 0
	totalNij = 0
	for patient in patient_data
		for combi in combination:
			for p in xrange(M):
				total_p += u[combi[0]][p]*u_inv[p][I]
			for q_i in xrange(M):
				total_q_i += u[I][q_i]*u_inv[q_i][combi[1]]
			for q_j in xrange(M):
				total_q_j += u[J][q_j]*u_inv[q_j][combi[1]]
	
	
			Akl += dpm.get_trainsition_probability(combi[0], combi[1], interval)

	totalRi += xpq*total_p*total_q_i/Akl
	totalNi = xpq*dpm.get_trainsition_probability(i, j, 1)*total_p*total_qj/Akl
	
	return totalRi, totalNi
