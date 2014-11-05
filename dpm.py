import numpy as np

class Dpm:
	def __init__(self, k, m, d):
		self.b = np.random.beta(1, 1, (2, k, m))
		self.l = np.random.beta(1, 1, d)
		self.z = np.random.beta(0.1, 1, (k, d))
		self.pi = np.random.random(m)
		self.q = np.random.random((m, m))
		self.x = np.random.randint(2 ,size=k)
                self.k = k
		self.m = m
		self.d = d
		for i in xrange(len(self.q)):
			self.q[i][i] = -np.sum(self.q[i][1:])

	def show_para(self):
		print 'Parameters'
		print self.pi

	def get_transition_probability(self, i, j, interval):
		return np.exp(self.q[i][j]*interval)

	def get_initial_probability(self):
		return self.pi

	def update_b(self, inc, k, m):
        	self.b[0][k][m] += float(inc)/100

	def update_l(self, inc, d):
		self.l[d] += float(inc)/100

	def update_z(self, inc, k, d):
		self.z[k][d] += float(inc)/100
