from numpy import linalg as LA
from numpy.linalg import inv

def get_eigen_decomposition(q, patient_data):
	interval = 10
	u, a = LA.eig(q)
	u_inv = inv(u)

	xpq = interval*np.exp(interval*a)

	total_p = 0
	for p in xrange(M):
		total_p += u[k][p]*u_inv[p][i]
	total_q = 0
	for q in xrange(M):
		total_q += u[i][q]*u_inv[q][l]
	
	Akl = dpm.get_trainsition_probability(k,l)
	totalRi = xpq*total_p*total_q/Akl
	totalNi = dpm.get_trainsition_probability(i, j)*totalRi

	return totalRi, totalNi

