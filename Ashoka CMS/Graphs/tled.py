import sys
import math
from itertools import combinations
import matplotlib.pyplot as plt
steps = []
times = []
ctr = 0
def nCr(n,r):
	f=math.factorial
	x= f(n)/f(r)/f(n-r)
	return x

for i in range (0,60):
	steps.append(i)
	times.append(nCr(60,i))

plt.plot(steps,times)
plt.ylabel('P(X)')
plt.show()