import random
import math

def getrandbit():
	return int(math.ceil(random.random()-0.5))

def getbinary(n):
	i=512;
	l = []
	while(i):
		l.append(n&i)
		i>>1
	return l

def getnumber(l):
	n=0
	for i,j in enumerate(l):
		n = n+j*(1<<(9-i))
	return n

def getbinarylist():
	i=0;
	l=[]
	while i<10:
		l.append(getrandbit())
		i += 1
	return l
def comp(a,b):
	return a[0]<b[0]
def get_val(n):	
	#let function is x^2 - 4
	return math.sin(n)

def cross(a,b):
	n = int(random.random()*10)
	x = a[:n]+b[n:]
	y = b[:n]+a[n:]
	return x,y
def mutate(child):
	n = int(random.random()*40)
	mutated = []
	#print "here"
	while len(mutated)<10:
		#print "aaaaaaaaa"
		while n in mutated:
			#print  "here"
			n = int(random.random()*40)
		m = int(random.random()*10)
		x = child[n][:]
		mutated.append(n)
		x[m] = 0 if x[m]==1 else 1;
		child.append(x)
	#print "done"

#gen list of 50
chromo = []
data = []

no_it = 100

while len(chromo)<50:
	chromo.append(getbinarylist())

data.append([getnumber(x) for x in chromo])
	
while no_it>0:
	

	
#selection
	best = []
	#print "chrom size : "+`len(chromo)`
	while len(best)<40:
		n = int(random.random()*50)
		while n in best:
			n = int(random.random()*50)
		m = int(random.random()*50)
		while m in best:
			m = int(random.random()*50)
	#	print `n`+' '+`m`+' '+"size: "+`len(chromo)`+'\n'
		if get_val(getnumber(chromo[n]))>get_val(getnumber(chromo[m])):
			best.append(chromo[n][:])
		else:
			best.append(chromo[m][:])
	#print "selection done !...best size:"+`len(best)`
#	for i in best:
#		print i
	i=0
	child = []

	while i<40:
		a,b = cross(best[i],best[i+1])
	#	print `a` + `b`+ '\n'
		child.append(a)
		child.append(b)
		i += 2;

	mutate(child);	
	#print "mutated....child size"+`len(child)`
	child = child+best
	#print '\nnew child size'+`len(child)`
	#val = {}
	val = []
	for i,x in enumerate(child):
		y = get_val(getnumber(x));
		val.append(tuple([y,x]))
	#print "val generated"
	val.sort(comp)
	chromo = []
	print '\n\n';
	print data
	data=[]
	for key in val:
		chromo.append(key[1][:])
	data.append([getnumber(x) for x in chromo])

	
	no_it -= 1
print '\n\n\n'+`[math.sin(i) for i in data[0]]`
