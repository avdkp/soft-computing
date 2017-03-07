import random as r
import math as m
points = [[r.random()*10,r.random()*10] for i in range(100)]
n = int(input("how many clusters:"))
center = [points[int(r.random()*len(points))][:] for i in range(n)]
no_it = 10
print 'points :\n'+`center`
def add(a,b):
	return [a[0]+b[0],a[1]+b[1]]
def cent(a,b):
	x = min([[m.sqrt((a[0]-c[0])**2+(a[1]-c[1])**2),i] for i,c in enumerate(b)])
	return x[1]

for t in range(no_it):
	cluster = [[] for i in range(n)]
	for i in points:
		cluster[cent(i,center)].append(i)
	center = []
	for c in cluster:
		if len(c)>0 :
			x = float( sum([ s[0] for s in c])/len(c))
		
			y = float(sum( [ s[1] for s in c])/len(c))
		center.append([x,y])
		#print '\n\n\n\n\n\n x is :'+`x`+', \nand Y is'+`y`
	print '\n\n'+`center`
print '\n\ncenters:'+`center`


