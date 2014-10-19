import numpy as np
import dpm, state, eigen

def read_synthetic_data(d, m):
	#Findings per states
	#Number of patients
	N = 10
	#Number of Visits
	V = 5

	patients = []
	for patient in xrange(10):
		patient_data = np.random.randint(2 ,size=(V, d))
		time_series = np.random.randint(10, size=V)
		patient_data = np.c_[time_series, patient_data]
		patients.append(patient_data)
        return patients

if __name__ == "__main__":

	#Set parameters
	K=10
	M=6
        D=20

        #Read patients data
        patients_data=read_synthetic_data(D, M)
         
	#Initialize Priors
        model = dpm.Dpm(K, M, D)
	
        #Optimization EM algorithm
	#E-step
	i = 0
	for patient in patients_data:
		#Make states
		j=0
		states = []
		for visit in patient:
		  comorbidities = np.random.randint(2,size=K)
                  s = state.State(comorbidities, visit[j])
		  states.append(s)
		  j+=1
		#Gibbs Sampling
                i += 1

	#Compute Cij
	i = 3
	j = 3

	Cij = 0
	for patient in patients_data:
		for visit in patient:
			Cij += model.get_transition_probability(i,j, visit[0])

	print Cij
        #M-step
	#update pi
	initiail_state = 1
	total_state_i = 0
	total_itnitial_state = 0
	
	for patient in patients_data:
		#Initial transition probabilty
		total_initial_state += dpm.get_trainsition_probability(i,j,1)
	"""
		for m in xrange(M):
			total_state_i += dpm.get_trainsition_probability(i,j)
	dpm.pi = total_initial_state/total_state_i


	#update Q
	old_q = dpm.q
	Nij, Ri = eigen.get_eigen_decomposition(dpm.q, patient_data)
	dpm.q = Nij/Ri

	#Check convergens
	if abs(old_q - dpm.q) < 0.01:
		print 'Finish' 
        """

