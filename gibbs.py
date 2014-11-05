
#%matplotlib inline 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import state, dpm

def get_psi(model, k, state, x, x_1):
	#b[0] = t-1
	tmp_0 = x*model.b[0][k][state]
	tmp_1 = (1-x)*(1-model.b[0][k][state])

	return tmp_0*tmp_1	

def get_phi(model, K, d, Od):
	calc_tmp = 1
	for k in xrange(K):
		calc_tmp =  calc_tmp*(1-model.x[k]*model.z[k][d])
	if int(Od[d]) == 1:
		pre = (1-(1-model.l[d]))*calc_tmp
		return pre*calc_tmp
	else:
		pre = 1-model.l[d]
		return pre*calc_tmp
        

def get_beta(model, k, O, state, t, i):
	res = 0
	for j in [0,1]:
        	o_pi = 1
		for d in xrange(len(O)):
                        o_pi = o_pi*get_phi(model, k, d, O[d])
		res_psi = get_psi(model, k, state, j, i)
		#res += get_beta(model, k, O, state, t+1, j)*res_psi*o_pi
		res += res_psi*o_pi
	return  res   

def get_sample_probability(model, findings, K, D, j, i):
	t = 5
	k = 5
	state = 1

	tmp_0 = get_beta(model, k, findings, state, t+1 ,j)/get_beta(model, k, findings, state, t, i)
        tmp_1 = get_psi(model, k, state, j, i)
	tmp_2 = 1
	for d in xrange(len(findings)):
		tmp_2 = tmp_2*get_phi(model, k, d, findings[d])

	return tmp_0*tmp_1*tmp_2

def gibbs_sampling(model, findings, K, D, j, i):
	p_old = get_sample_probability(model, findings, K, D, j, i)
	for inc in xrange(1000):
		for k in xrange(K):
			for m in xrange(M):
				model.update_b(inc, k, m)
				p_new = get_sample_probability(model, findings, K, D, j, i)
				if p_new/p_old > 1:
					p_old = p_new
				else:
					break

		for k in xrange(K):
			for d in xrange(D):
				model.update_z(inc, k, d)
				p_new = get_sample_probability(model, findings, K, D, j, i)
				if p_new/p_old > 1:
					p_old = p_new
				else:
					break           

		for d in xrange(D):
			model.update_l(inc, d)
			p_new = get_sample_probability(model, findings, K, D, j, i)
			if p_new/p_old > 1:
				p_old = p_new
			else:
				break           

	print "Finish Sampling"

if __name__ == "__main__":
 	#Set parameters
	K=10
	M=6
        D=20
	j = 1
	i = 0

	#Initialize Priors
        model = dpm.Dpm(K, M, D)
	

	findings = np.random.randint(2 ,size=(1, D)) 
	gibbs_sampling(model, findings, K, D, j, i)
