import random as r
import copy
import matplotlib.pyplot as plt

def compare(r1,r2,c1,c2):
	if r1<r2:
		return True
	if r1==r2 and c1>c2:
		return True
	return False
def select(pop,rank,CD):
	global pop_size
	selected = set([])
	mu = r.random()
	while len(selected)<pop_size:
		i = int(r.random()*pop_size)
		j = int(r.random()*pop_size)
		if compare(rank[pop[i]],rank[pop[j]],CD[pop[i]],CD[pop[j]]):
			selected.add(pop[i])
		else:
			selected.add(pop[j])
	return selected
def cross(selected):
	global pop_size
	child = set([])
	mu = r.random()
	para = 1/(1+mu)
	while len(child)<len(selected):
		b = (2*r.random())**para if r.random()<0.5 else ((1/(2*(1-r.random())))**para)
		l = len(child)
		c1 = 0.5*((1-b)*selected[l]+(1+b)*selected[l+1])
		child.add(c1)
		c2 = 0.5*((1+b)*selected[l]+(1-b)*selected[l+1])
		if len(selected)>len(child):
			child.add(c2)
	return child
def mutation(child):
	for i in range(int(0.1*len(child))):
		j = int(r.random()*len(child))
		mu = r.random()
		para = 1/(1+mu)
		d = (2*r.random())**para -1 if r.random()<0.5 else (1 - (2*(1-r.random()))**para)
		child[j] = (child[j]+d) if child[j]+d < 5 and child[j]+d >5 else (r.random()-0.5)*10
	return child
def get_val(x,f):
	if f==1:
		return x**2
	elif f==2:
		return (x-2)**2
	else:
		pass
def dominates(p,q):
	if get_val(p,1)>get_val(q,1) or get_val(p,2)>get_val(q,2):
		return False
	return True
def non_dominated_sort(P):
	S={}
	n={}
	rank={}
	F=[]
	F.append(0)
	F.append(set([]))
	#print `len(P)`
	for p in P:
		S[p]=set([])
		n[p]=0
		for q in P:
			if dominates(p,q):
				S[p].add(q)
			elif dominates(q,p):
				n[p]+=1
			else:
				pass
		if n[p]==0:
			rank[p]=1
			F[1].add(p)
	i=1
	while len(F[i])>0:
		Q=set([])
		for p in F[i]:
			for q in S[p]:
				n[q] -= 1
				if n[q]==0:
					rank[q]=i+1
					Q.add(q)
		i+=1
		F.append(Q)
	return rank
def rank_wise_func(ranking):
	rank_wise={}
	for key,val in ranking.iteritems():
		if val in rank_wise:
			rank_wise[val].append(key)
		else:
			rank_wise[val]=[]
			rank_wise[val].append(key)
	return rank_wise
def comp1(a,b):
	return True if (b[0]>a[0] or (b[0]==a[0] and a[1]>b[1])) else False
def crowding_dist(rank_wise):
	global m
	CD={}
	for key,val in rank_wise.iteritems():
		for i in range(m):
			val1 = [[get_val(a,i+1),a] for a in val]
			val1.sort()
			CD[val1[0][1]]=float("inf")
			CD[val1[len(val1)-1][1]]=float("inf")
			for j in range(1,len(val1)-1):
				if not val1[j][1] in CD:
					CD[val1[j][1]] = 0
				CD[val1[j][1]] += (val1[j+1][0]-val1[j-1][0])/(val1[len(val1)-1][0]-val1[0][0])
	return CD
no_it=10
pop_size=100
m=2
pop_range = [-5,5]
rank_wise = {}
pop=set([])
while len(pop)<pop_size:
	pop.add((r.random()-0.5)*10)
first = list(pop)
pop = list(pop)
for i in range(no_it):
	rank=non_dominated_sort(pop)
	rank_wise=rank_wise_func(rank)
	CD = crowding_dist(rank_wise)
	for key,val in rank_wise.iteritems():
		aa = [[CD[a],a] for a in val]
		aa.sort()
		#print `key`+" "+`aa`
	#print CD
	if len(rank_wise[1])==pop_size:
		print CD
		break
	selected = list(select(pop,rank,CD))
	child = list(cross(selected))
	mutated = mutation(child)
	pop_full = selected+mutated
	ranking = non_dominated_sort(pop_full)
	rank_wise = rank_wise_func(ranking)
	CD = crowding_dist(rank_wise)
	pop=set([])
	bb=[]
	bb = [[ranking[a],CD[a],a] for a in pop_full]
	bb.sort(comp1)
	pop=set([])
	#print "hello"
	for a in bb:
		if len(pop)<pop_size:
			pop.add(a[2])
	pop = list(pop)
#	for key,val in 
plt.figure()
pop = list(pop)
plt.scatter([get_val(a,1) for a in first],[get_val(a,2) for a in first],label = 'first gen',color="r")
plt.scatter([get_val(a,1) for a in pop],[get_val(a,2) for a in pop],label = 'last gen',color="b")
plt.legend()
plt.show()
