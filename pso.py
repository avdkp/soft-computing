import random as r
import copy as cp
import matplotlib.pyplot as plt

pop_size=50
c1 = 2
c2 = 2
w = 0.9
max_val = 100		#-50 t0 +50
no_it = 100

def get_val(a):
	return a[0]**2+a[1]**2

pop = [[(r.random()-0.5)*max_val,(r.random()-0.5)*max_val] for i in range(pop_size)]
vel = [[(r.random()-0.5)*max_val,(r.random()-0.5)*max_val] for i in range(pop_size)]

pbest = cp.deepcopy(pop)
y = map(get_val,pop)
x = map(None,y,pop)
#print x
gbest = min(x)[1]
print gbest
plt.plot(map(get_val,pop))
for i in range(no_it):
	for j in range(pop_size):
		f = [w*a for a in vel[j]]
		s1 = [a-b for a,b in zip(pbest[j],pop[j])]
		s = [c1*r.random()*t for t in s1]
		t1 = [a-b for a,b in zip(gbest,pop[j])]
		t = [c2*r.random()*t for t in t1]
		vel[j] = [a+b+c for a,b,c in zip(f,s,t)]
		pop[j] = [a+b for a,b in zip(pop[j],vel[j])]
		pbest[j] = pbest[j] if get_val(pbest[j])<get_val(pop[j]) else pop[j][:]
		y = map(get_val,pop)
		x = map(None,y,pop)
		gbest = gbest if gbest<min(x)[0] else min(x)[1][:]
	w = 0.4# w - ((0.9-0.4)/(no_it))
#ff = [1 for i in range(pop_size)]
plt.plot(-500)
plt.plot(map(get_val,pop))
print pop
plt.show()
