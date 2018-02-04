import numpy as np
from scipy.optimize import fmin
import math

def f(x1,x2):
	return(1.5*(x1**2) + x2**2 - 2*x1*x2 + 0.5*(x1**4))

def d1(x1,x2):
	return (3*x1 - 2*x2 + 6*(x1**2) + 2*(x1**3))

def d2(x1,x2):
	return (2*x2 - 2*x1)

x = np.array([1,-3])
learningRate = 0.00001
theta = 0.0001
maxIters = 100000
exit = False
iter = 0
minVal = f(x[0],x[1])


while exit == False:
	df = np.array([d1(x[0],x[1]),d2(x[0],x[1])])
	x = x - learningRate * df
	# print (str(x) + " " + str(f(x[0],x[1])) + " " + str(df[0]) + " " + str(df[1]))
	if abs(x.any()) < theta: exit = True;
	if iter > maxIters : exit = True
	if minVal < f(x[0],x[1]) : exit = True;
	minVal = f(x[0],x[1]);
	iter = iter +1


print (iter)
print (minVal)

def f1(x):
	return(1.5*(x[0]**2) + x[1]**2 - 2*x[0]*x[1] + 0.5*(x[0]**4))

min = fmin(f1,x)