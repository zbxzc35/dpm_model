#%matplotlib inline 
import matplotlib.pyplot as plt
import pymc as pm
import numpy as np
import pandas as pd
import state

k = 10
d = 1
findings = np.random.normal(1, scale=1, size=(k, d))

"""
xtrue = np.random.randint(2,size=k)
ztrue = np.random.normal(1, scale=1, size=(k, d))
ltrue = np.random.normal(1, scale=1, size=d)
odata = 1-(1-ltrue)*(1-xtrue*ztrue) 
"""

state1 = state.State(k, d, findings)


#odata = np.random.normal(loc=o_eq, scale=.75, size=(k, d))

def gibbs_sampling(model, findings):
	with pm.Model() as model:
		#priors
		x = pm.Normal('x', mu=0., sd=1)    
		z = pm.Normal('z', mu=1, sd=2., shape=(k, d))    
		l = pm.Normal('l', mu=1, sd=2., shape=d)    
		o_eq = 1-(1-l)*(1-x*z)

	o = pm.Normal('o', mu=o_eq, sd=.75, observed=findings)


	with model:    
		start = pm.find_MAP()
		step = pm.NUTS()
		trace = pm.sample(10000, step, start)

	pm.traceplot(trace).savefig("build/TEST.png")
