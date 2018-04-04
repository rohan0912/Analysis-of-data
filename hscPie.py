import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from data import *
s1=s2=s3=s4=s5=n=0
for a1,b1,c1,d1,e1,a2,b2,c2,d2,e2,a3,b3,c3,d3,e3 in zip(p1,p2,p3,p4,p5,c1,c2,c3,c4,c5,b1,b2,b3,b4,b5):
  if a1>50 and a2>50 and a3 >50:
    s1+=1
  if b1>50 and b2>50 and b3 >50:
    s2+=1
  if c1>50 and c2>50 and c3 >50:
    s3+=1
  if d1>50 and d2>50 and d3 >50:
    s4+=1
  if e1>50 and e2>50 and e3 >50:
    s5+=1
  n+=1
s1=s1*100/n
s2=s2*100/n
s3=s3*100/n
s4=s4*100/n
s5=s5*100/n

labels=[2011,2012,2013,2014,2015]
size=[s1,s2,s3,s4,s5]
explode=(0,0.1,0,0,0)
print(type(s1))
fig1, ax1=plt.subplots()
ax1.set_title('Graph for no. of students qualified for NEET')
ax1.pie(size,explode=explode,labels=labels,autopct='%1.2f%%',shadow=True,startangle=90)
ax1.axis('equal')
plt.show()

s1=(int)(s1);s2=(int)(s2);s3=(int)(s3);s4=(int)(s4);s5=(int)(s5);n=(int)(n)

s1=s2=s3=s4=s5=n=0
print(type(s1))
for a1,b1,c1,d1,e1,a2,b2,c2,d2,e2,a3,b3,c3,d3,e3 in zip(p1,p2,p3,p4,p5,c1,c2,c3,c4,c5,m1,m2,m3,m4,m5):
  if a1>50 and a2>50 and a3 >50:
    s1+=1
  if b1>50 and b2>50 and b3 >50:
    s2+=1
  if c1>50 and c2>50 and c3 >50:
    s3+=1
  if d1>50 and d2>50 and d3 >50:
    s4+=1
  if e1>50 and e2>50 and e3 >50:
    s5+=1
  n+=1
s1=s1*100/n
s2=s2*100/n
s3=s3*100/n
s4=s4*100/n
s5=s5*100/n

labels=[2011,2012,2013,2014,2015]
size=[s1,s2,s3,s4,s5]
explode=(0,0.1,0,0,0)

fig1, ax1=plt.subplots()
ax1.set_title('Graph for no. of students qualified for JEE MAINS')
ax1.pie(size,explode=explode,labels=labels,autopct='%1.2f%%',shadow=True,startangle=90)
ax1.axis('equal')
plt.show()
