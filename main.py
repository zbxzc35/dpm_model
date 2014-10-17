import numpy as np
import dpm,state

def read_synthetic_data(d, m):
	#Findings per states
	N = 10
	patients = np.random.randint(2 ,size=(N, m, d))
        return patients

if __name__ == "__main__":

	#Set parameters
	K=10
	M=6
        D=20

        #Read patients data
        patients_data=read_synthetic_data(D, M)
         
	#Initialize Priors
        dpm.Dpm(K, M, D)
	
        #Optimization EM algorithm
	#E-step
	i = 0
	for patient in patients_data:
		#Make states
		j=0
		states = []
		for visit in patients_data[i]:
		  comorbidities = np.random.randint(2,size=K)
                  s = state.State(comorbidities, visit[j])
		  states.append(s)
		  j+=1
		#Gibbs Sampling
                i += 1

	#Compute Cij
	i = 3
	j = 3

	for patient in patients_data:
		for m in xrange(M):
			dpm.get_trainsition_probability(i,j)

        #M-step
	#update pi
	print dpm.get_trainsition_probability(1,1)


	#update Q


	#Check convergens

