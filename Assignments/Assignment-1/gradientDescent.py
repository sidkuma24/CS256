import numpy as np
import math

def f(x1,x2):
	return(1.5*(x1**2) + x2**2 - 2*x1*x2 + 2*x1**3 + 0.5*(x1**4))

def d1(x1,x2):
	return (3*x1 - 2*x2 + 6*(x1**2) + 2*(x1**3))

def d2(x1,x2):
	return (2*x2 - 2*x1)

x = np.array([1,-3])
learningRate = 0.1
theta = 0.001
maxIters = 200
exit = False
niter = 0
minVal = f(x[0],x[1])
print (str(x) + " " + str(f(x[0],x[1])) + " " + str(d1(x[0],x[1])) + " " + str(d2(x[0],x[1])))
df = np.array([d1(x[0],x[1]),d2(x[0],x[1])])

while exit == False:
	if abs(x.any()) < theta: exit = True;
	if niter > maxIters : exit = True
	x = x - learningRate * df
	df = np.array([d1(x[0],x[1]),d2(x[0],x[1])])
	print (str(x) + " " + str(f(x[0],x[1])) + " " + str(df[0]) + " " + str(df[1]))
	niter += 1


print ("No of iterations: ",niter)
print ("Minval : ",f(x[0],x[1]))

