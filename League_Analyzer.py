import numpy as np
from numpy.random import random_sample

def weighted_values(values, probabilities, size):
    bins = np.add.accumulate(probabilities)
    return values[np.digitize(random_sample(size), bins)]
var1=int(input("enter your LP for win as a positive integer"))
var2=int(input("enter your LP for loss as a positive integer"))
var3=float(input("enter your probability of winning as a decimal"))
values = np.array([var1,-var2])
probabilities = np.array([var3,float(1)-var3])
i=0
ja=0
j=0
n=1
m=[]
so=[]
f=(weighted_values(values, probabilities, 1000000))
while i<len(f):
    ja+=f[i]
    if ja>=100:
        ja=0
        if i<len(f)-1:
            if f[i]+f[i+1]==values[0]*2:
                m.append(i)
        if i<len(f)-2:
            if f[i]+f[i+2]==values[0]*2:
                m.append(i)
            if f[i+1]+f[i+2]==values[0]*2:
                m.append(i)
    i+=1
while n<len(m)-1:
    if m[n]!=m[n+1]:
        so.append(m[n+1]-m[n]+2)
    n+=1
mu=int(sum(so)/len(so))
max=0
print(str(mu)+" game average to rank up")
