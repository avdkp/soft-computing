import random as r
import copy
import matplotlib.pyplot as plt

def compare(r1,r2,c1,c2):
	return True if ((r1==r2 and c1>c2) or r1<r2) else False
def select(pop,rank,CD):
	global pop_size
	selected = set([])
	mu = r.random()
	while len(selected)<pop_size:
		i,j = int(r.random()*pop_size),int(r.random()*pop_size
		if compare(rank[pop[i]],rank[pop[j]],CD[pop[i]],CD[pop[j]]):
			selected.add(pop[i])
		else:
			selected.add(pop[j])
	return selected
def cross(selected):
	global pop_size
	child,para = set([]),1/(1+r.random())
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
		j,para = int(r.random()*len(child)),1/(1+r.random())
		d = (2*r.random())**para -1 if r.random()<0.5 else (1 - (2*(1-r.random()))**para)
		child[j] = (child[j]+d) if child[j]+d < 5 and child[j]+d >5 else (r.random()-0.5)*10
	return child
def get_val(x,f):
	return x**2 if f==1 else (x-2)**2
def dominates(p,q):
	if get_val(p,1)>get_val(q,1) or get_val(p,2)>get_val(q,2):
		return False
	return True
def non_dominated_sort(P):
	S,n,F,rank={},{},[],{}
	F.append(0)
	F.append(set([]))
	for p in P:
		S[p],n[p]=set([]),0
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
def crowding_dist(rank_wise):
	global m
	CD={}
	for key,val in rank_wise.iteritems():
		for i in range(m):
			val1 = [[get_val(a,i+1),a] for a in val]
			val1.sort()
			CD[val1[0][1]],CD[val1[len(val1)-1][1]]=float("inf"),float("inf")
			for j in range(1,len(val1)-1):
				if not val1[j][1] in CD:
					CD[val1[j][1]] = 0
				CD[val1[j][1]] += (val1[j+1][0]-val1[j-1][0])/(val1[len(val1)-1][0]-val1[0][0])
	return CD
no_it=10
pop_size=100
m=2
rank_wise = {}
pop=set([])
while len(pop)<pop_size:
	pop.add((r.random()-0.5)*10)
pop = list(pop)
first = pop
for i in range(no_it):
	rank=non_dominated_sort(pop)
	rank_wise={}
	for key,val in rank.iteritems():
		if val in rank_wise:
			rank_wise[val].append(key)
		else:
			rank_wise[val]=[]
			rank_wise[val].append(key)
	if len(rank_wise[1])==pop_size:
		print CD
		break
	CD = crowding_dist(rank_wise)
	selected = list(select(pop,rank,CD))
	child = list(cross(selected))
	mutated = mutation(child)
	pop_full = selected+mutated
	ranking = non_dominated_sort(pop_full)
	pop=set([])
	aa = [[ranking[a],a] for a in pop_full]
	aa.sort()
	pop=set([])
	for a in aa:
		if len(pop)<pop_size:
			pop.add(a[1])
	pop = list(pop)
plt.figure()
plt.scatter([get_val(a,1) for a in first],[get_val(a,2) for a in first],label = 'first gen',color="r")
plt.scatter([get_val(a,1) for a in pop],[get_val(a,2) for a in pop],label = 'last gen',color="b")
plt.legend()
plt.show()
