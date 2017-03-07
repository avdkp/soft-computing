import random as r
import copy

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
	while bool(F[i]):
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
		#	print `len(val1)`+" --->>>>>>>"
			CD[val1[0][1]]=float("inf")
			CD[val1[len(val1)-1][1]]=float("inf")
			for j in range(1,len(val1)-1):
				if not val1[j][1] in CD:
					CD[val1[j][1]] = 0
				CD[val1[j][1]] += (val1[j+1][0]-val1[j-1][0])/(val1[len(val1)-1][0]-val1[0][0])
	return CD
no_it=100
pop_size=100
m=2
pop_all={}
pop_range = [-5,5]
rank_wise = {}
pop=set([])
while len(pop)<pop_size:
	pop.add((r.random()-0.5)*5)
for i in pop:
	pop_all[i]=(get_val(i,1),get_val(i,2))
rank=non_dominated_sort(pop)
print "RANK "+`rank`
#rank_wise=[[] for i in range(len(rank)+1)]
for key,val in rank.iteritems():
	if val in rank_wise:
		rank_wise[val].append(key)
	else:
		rank_wise[val]=[]
		rank_wise[val].append(key)
print "ran "+`rank_wise`
crowding_dist(rank_wise)

#for i in range(no_it):
	
