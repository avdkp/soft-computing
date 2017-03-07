import random as r
import copy
import matplotlib.pyplot as mt
def get_val(a):
	#print a
	return a[0]**2+a[1]**2+a[2]**2
def getbest(x):
	a=[copy.deepcopy(x) for i in range(5)]
	x = max([[get_val(a[i]),i] for i in range(len(a))])	
	return a[x[1]]
def shuffle(pos,vel):
	for i in range(100):
		x = r.randint(0,99)
		y = r.randint(0,99)
		pos[x],pos[y] = pos[y],pos[x]
		vel[x],vel[y] = pos[y],pos[x]
pop = 100
it = 10000
c1 = 2
w = 0.4

vel =  [[r.random(),r.random(),r.random()] for i in range(pop)]
pos =  [[r.random(),r.random(),r.random()] for i in range(pop)]
x = max([[get_val(a),a] for a in pos])
gbest = x[1][:]


for i in range(it):
	for j in range(int(pop*0.8)):
		pos[j] = getbest(pos[j])
	for j in range(int(pop*0.8),pop):
		vel[j] = [x*w+2*r.random()*(gx-px) for x,gx,px in zip(vel[j],gbest,pos[j])]
		pos[j] = [x+v for x,v in zip(pos[j],vel[j])]
		shuffle(pos,vel)
mt.plot([get_val(a) for a in pos])
mt.show()
