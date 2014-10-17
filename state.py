import numpy as np

class State:
	def __init__(self, comorbidities, findings):
		print 'State'
		self.comorbidities = comorbidities
		self.findings = findings  

	def show_info(self):
		print 'comorbidities = %s' % self.comorbidities

if __name__ == "__main__":
	k=1
	d=2

	findings=np.random.normal(1, scale=1, size=(k, d))
	comorbidities=np.random.normal(1, scale=1, size=(k, d))

	p1 = State(comorbidities, findings)
	p1.show_info()

	states=[]
	states.append(p1)
