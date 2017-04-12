import random as r
import math as m
in_count = 2
hid_c = 20 
out_c = 1
mu = 0.2

win = [[(r.random()-0.5)*2 for b in range(hid_c)] for a in range(in_count)]
wout = [(r.random()-0.5)*2 for b in range(hid_c)]
#bias = [r.random() for a in range(hid_c)]

def sig_1_s(a):
	#return a
	return 1/(1+m.exp(-a))

def output(in0,in1):
	global win,hid_c,wout
	hid1 = [in0*i for i in win[0]]
	hid2 = [in1*i for i in win[1]]
	hid = [a+b for a,b in zip(hid1,hid2)]
	hid = map(sig_1_s,hid)

	out = sum([a*b for a,b in zip(hid,wout)])
	return sig_1_s(out)

def train(in0,in1,tar):
	global mu,win,wout
	hid1 = [in0*i for i in win[0]]
	hid2 = [in1*i for i in win[1]]
	hid = [a+b for a,b in zip(hid1,hid2)]
	hid = map(sig_1_s,hid)

	out = sum([a*b for a,b in zip(hid,wout)])
	out = sig_1_s(out)
	delta = out*(1-out)*(tar-out)
	wout = [a+mu*b*delta for a,b in zip(wout,hid)]
	hid_delta = [w*delta*h*(1-h) for w,h in zip(wout,hid)]

	win[0] = [w+mu*d*in0 for w,d in zip(win[0],hid_delta)]
	win[1] = [w+mu*d*in1 for w,d in zip(win[1],hid_delta)]

#	print `in0` + " " + `in1` + " " + `output(in0, in1)` + " " + `tar`

print output(0.2,0.3)

for i in range(100000):
	a = r.random()
	b = r.random()
	train(a,b,a+b)
	print i
print output(0.5,0.5)

print output(0,0)

print output(0.9,0.9)
print output(0.1,0.9)





