import numpy as np
import dpm,state

def read_synthetic_data(d, m):
	N = 10
	patients = np.random.randint(2,size=(m,n,d))
        return patients

if __name__ == "__main__":

	#Set parameters
	k=10
	M=6
        d=10

        #Read patients data
        patients_data=read_synthetic_data(d, m)
         
	#Initialize Priors
        dpm.Dpm(k, m, d)
	
        #Optimization EM algorithm
	#E-step
	for patient in patients_data:
		#Make states
		for state in patient:

		#Gibbs Sampling


        #M-step
	#update pi


	#update Q

	#Check convergens

