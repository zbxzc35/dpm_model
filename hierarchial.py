#%matplotlib inline 
import matplotlib.pyplot as plt
import pymc as pm
import numpy as np
import pandas as pd
import state, dpm

"""
k = 10
d = 1
findings = np.random.normal(1, scale=1, size=(k, d))

xtrue = np.random.randint(2,size=k)
ztrue = np.random.normal(1, scale=1, size=(k, d))
ltrue = np.random.normal(1, scale=1, size=d)
odata = 1-(1-ltrue)*(1-xtrue*ztrue) 
"""


#odata = np.random.normal(loc=o_eq, scale=.75, size=(k, d))

def gibbs_sampling(model, findings, K, D):
	"""
	with pm.Model() as model:
		#priors
		#x = pm.Normal('x', mu=0., sd=1, shape= K)    
		#z = pm.Normal('z', mu=1, sd=2., shape= (K,1))    
		l = pm.Normal('l', mu=1, sd=2., shape=1)

		#o_eq = 1-(1-l)*(1-x*z)
		#Hold
		b = np.empty(K, dtype=object)
		z = np.empty(K, dtype=object)

		for i in range(len(b)):
			b[i] = pm.Normal("b" + str(i + 1), 0, 0.0001)

                for i in range(len(z)):
			z[i] = pm.Normal("z" + str(i + 1), 0, 0.0001)  

		#o_eq = 1-(1-l)*(1-b*z)

		print '------'

	o = pm.Normal('o', mu=o_eq, sd=.75, observed=findings)


	with model:    
		start = pm.find_MAP()
		step = pm.NUTS()
		trace = pm.sample(10000, step, start)

	pm.traceplot(trace).savefig("build/TEST.png")
        """
if __name__ == "__main__":
 	#Set parameters
	K=10
	M=6
        D=20

	#Initialize Priors
        model = dpm.Dpm(K, M, D)
	

	findings = np.random.normal(1, scale=1, size=D)
	gibbs_sampling(model, findings, K, D)
