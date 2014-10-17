import numpy as np

class Dpm:
	def __init__(self, k, m, d):
		self.b = np.random.beta(1, 1, (2, k, m))
		self.l = np.random.beta(1, 1, d)
		self.z = np.random.beta(0.1, 1, (k, d))
		self.pi = np.random.random(m)
		self.q = np.random.random((m, m))
	def show_para(self):
		print 'Parameters'
		print self.pi

	def get_transition_probability(self, i, j):
		return np.exp(self.q[i][j])


		
	
