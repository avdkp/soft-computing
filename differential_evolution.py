import random
NP = 15
F = 1
CR = 0.3
no_it = 1000
target = [[(random.random()-0.5)*10.24,(random.random()-0.5)*10.24,(random.random()-0.5)*10.24] for i in range(0,NP)]
for x in range(0,no_it):
	trial = [[x if random.random()>=CR else y for x,y in zip(target[i],[a+F*(b-c) for a,b,c in zip(target[i],target[int(random.random()*NP)],target[int(random.random()*NP)]) for t in range(0,3) ]) ] for i in  range(0,NP)]
	target = [target[i] if (target[i][0]**2+target[i][1]**2+target[i][2]**2)<(trial[i][0]**2+trial[i][1]**2+trial[i][2]**2) else trial[i]  for i in range(0,NP)]
	print '\n\n\n\n'+`target`
