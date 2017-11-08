import sys
import math
from itertools import combinations
import matplotlib.pyplot as plt
steps = []
Px = []
ctr = 0
def nCr(n,r):
	f=math.factorial
	x= f(n)/f(r)/f(n-r)
	return x

for i in range (0,63):
	steps.append(i)
	Px.append(nCr(63,i))

plt.plot(steps,Px)
plt.ylabel('P(X)')
plt.show()
