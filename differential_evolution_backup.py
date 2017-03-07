import random
NP = 50 
F = 0.5
CR = 0.3
no_it = 10000
def get_vec():
	return [(random.random()-0.5)*10.24,int(random.random()-0.5)*10.24,(random.random()-0.5)*10.24]
def get_val(n):
	return n[0]*n[0]+n[1]*n[1]+n[2]*n[2]
target = [get_vec() for i in range(0,NP)]
for x in range(0,no_it):
	mutant = [[target[i][k]+[F*(target[int(random.random()*NP)][j]-target[int(random.random()*NP)][j]) for j in range(0,3)][k] for k in range(0,3)] for i in range(0,NP)]
	trial = [[ mutant[i][0] if random.random()<CR else target[i][0],  mutant[i][1] if random.random()<CR else target[i][1], mutant[i][2] if random.random()<CR else target[i][2]]  for i in range(0,NP)]
	target = [target[i] if get_val(target[i])<get_val(trial[i]) else trial[i]  for i in range(0,NP)]
print target
