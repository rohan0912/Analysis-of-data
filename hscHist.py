import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from data import *

x=np.arange(3)


#hindi
N=5
nd=np.arange(N)
width=0.18
fig=plt.figure()
ax=fig.add_subplot(111)
s1=s2=s3=s4=s5=n=0
#3rd div 
for a,b,c,d,e in zip(h1,h2,h3,h4,h5):
  if a >=40 and a<50:
    s1+=1
  if b >=40 and b<50:
    s2+=1
  if c >=40 and c<50:
    s3+=1
  if d >=40 and d<50:
    s4+=1
  if e >=40 and e<50:
    s5+=1
l1=[s1,s2,s3,s4,s5]
print(l1)
bin=[2011,2012,2013,2014,2015]
plt.hist(l1,histtype='stepfilled',bins=5)
plt.show()
