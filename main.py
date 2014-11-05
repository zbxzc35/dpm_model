import numpy as np
import dpm, state, eigen, gibbs

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
	
	print model.q.shape

        #Make state
	"""
	j_v= 0
	states = []
	for visit in patient:
		  comorbidities = np.random.randint(2,size=K)
                  s = state.State(comorbidities, visit[j_v])
		  states.append(s)
	"""

        #Optimization EM algorithm
	while True:
		#E-step
		for i in xrange(M):
			for j in xrange(M):
				for patient in patients_data:
						for findings in patient:
							#Gibbs Sampling
							gibbs.gibbs_sampling(model, findings[1:], K, D, M, 1, 0)

				#Compute Cij
				Cij = 0
				for patient in patients_data:
					for visit in patient:
						Cij += model.get_transition_probability(i, j, visit[0])

				print 'Cij = %s' % Cij

        			#M-step
				#UPDATE pi
				initiail_state = 1
				total_state_i = 0

				for stage in xrange(M):
					total_initial_state = 0
					for patient in patients_data:
						#Initial transition probabilty
						total_initial_state += model.get_initial_probability()[stage]
					mode_total_initial_state = 0	
					for mode in xrange(M):
						mode_total_initial_state += model.get_initial_probability()[mode]
					model.pi[stage] = total_initial_state/mode_total_initial_state

				#UPDATE Q
				old_q = model.q
				Nij, Ri = eigen.get_eigen_decomposition(model, patients_data, M, i, j)
				model.q[i][j] = Nij/Ri

		#Check convergens
		if fabs(old_q - model.q) < 0.0001:
			break
			print 'Finish' 
