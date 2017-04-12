import random as r

mu = 10.0
def get_val(a):
	return a**2
def mutate(a):
	global mu
	ra = r.random()
	d = ((2*ra)**(1/(1+mu)))-1 if ra<=0.5 else 1-(2*(1-r.random()))**(1/(1+mu))
	return a+d if abs(a+d)<20 else (r.random()-0.5)*40
	
test = r.random()*10

pop = [(r.random()-0.5)*40 for i in range(50)]
it = 100
for i in range(it):
	best = min([[get_val(a),a] for a in pop])
	clone = [mutate(best[1]) for j in pop]
	mutated = clone #map(mutate,clone)
	pop = pop+mutated
	pop1 = [[get_val(a),a] for a in pop]
	pop1.sort()
	pop = pop1[:50]
	pop = [a[1] for a in pop]
result = map(abs, pop) 
for a in result:
	print a


	
