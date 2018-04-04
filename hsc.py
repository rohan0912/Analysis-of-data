import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from data import *
d1=d[['Physics','Chemistry','Maths']]

s1=s2=s3=s4=s5=n=0
#pass in hin
for a,b,c,d,e in zip(h1,h2,h3,h4,h5):
  if a >=40:
    s1+=1
  if b >=40 :
    s2+=1
  if c >=40 :
    s3+=1
  if d >=40:
    s4+=1
  if e >=40 :
    s5+=1
  n+=1
  
#fail
f1=n-s1;f2=n-s2;f3=n-s3;f4=n-s4;f5=n-s5
#graph for pass and fail
N=5
nd=np.arange(N)
width=0.3
fig=plt.figure()
ax=fig.add_subplot(111)
l=[s1,s2,s3,s4,s5]
r1=ax.barh(nd+width,l,width,color='g')
l1=[f1,f2,f3,f4,f5]
r2=ax.barh(nd+width*2,l1,width,color='magenta')
ax.set_xlabel("No. of students")
ax.set_yticks(nd+width)
ax.set_yticklabels(('2011','2012','2013','2014','2015'))
ax.legend((r1[0],r2[0]),('Pass in Hindi','Fail in Hindi'))

def al(r):
  for i in r:
    h=i.get_y()+i.get_height()
    w=i.get_x()+i.get_width()
    ax.text(i.get_x()+i.get_width()/2,1.05*h,'%d'%int(w),ha='left',va='top')
al(r1);al(r2)
plt.show()

s1=s2=s3=s4=s5=n=0
#pass in eng
for a,b,c,d,e in zip(e1,e2,e3,e4,e5):
  if a >=40:
    s1+=1
  if b >=40 :
    s2+=1
  if c >=40 :
    s3+=1
  if d >=40:
    s4+=1
  if e >=40 :
    s5+=1
  n+=1
  
#fail
f1=n-s1;f2=n-s2;f3=n-s3;f4=n-s4;f5=n-s5
#graph for pass and fail
N=5
nd=np.arange(N)
width=0.3
fig=plt.figure()
ax=fig.add_subplot(111)
l=[s1,s2,s3,s4,s5]
r1=ax.barh(nd+width,l,width,color='lightblue')
l1=[f1,f2,f3,f4,f5]
r2=ax.barh(nd+width*2,l1,width,color='violet')
ax.set_xlabel("No. of students")
ax.set_yticks(nd+width)
ax.set_yticklabels(('2011','2012','2013','2014','2015'))
ax.legend((r1[0],r2[0]),('Pass in English','Fail in English'))

def al(r):
  for i in r:
    h=i.get_y()+i.get_height()
    w=i.get_x()+i.get_width()
    ax.text(i.get_x()+i.get_width()/2,1.05*h,'%d'%int(w),ha='left',va='top')
al(r1);al(r2)
plt.show()


s1=s2=s3=s4=s5=n=0
#pass in bio
for a,b,c,d,e in zip(b1,b2,b3,b4,b5):
  if a >=40:
    s1+=1
  if b >=40 :
    s2+=1
  if c >=40 :
    s3+=1
  if d >=40:
    s4+=1
  if e >=40 :
    s5+=1
  n+=1
  
#fail
f1=n-s1;f2=n-s2;f3=n-s3;f4=n-s4;f5=n-s5
#graph for pass and fail
N=5
nd=np.arange(N)
width=0.3
fig=plt.figure()
ax=fig.add_subplot(111)
l=[s1,s2,s3,s4,s5]
r1=ax.barh(nd+width,l,width,color='pink')
l1=[f1,f2,f3,f4,f5]
r2=ax.barh(nd+width*2,l1,width,color='lightgreen')
ax.set_xlabel("No. of students")
ax.set_yticks(nd+width)
ax.set_yticklabels(('2011','2012','2013','2014','2015'))
ax.legend((r1[0],r2[0]),('Pass in Biology','Fail in Biology'))

def al(r):
  for i in r:
    h=i.get_y()+i.get_height()
    w=i.get_x()+i.get_width()
    ax.text(i.get_x()+i.get_width()/2,1.05*h,'%d'%int(w),ha='left',va='top')
al(r1);al(r2)
plt.show()

s1=s2=s3=s4=s5=n=0
#pass in phy
for a,b,c,d,e in zip(p1,p2,p3,p4,p5):
  if a >=40:
    s1+=1
  if b >=40 :
    s2+=1
  if c >=40 :
    s3+=1
  if d >=40:
    s4+=1
  if e >=40 :
    s5+=1
  n+=1
  
#fail
f1=n-s1;f2=n-s2;f3=n-s3;f4=n-s4;f5=n-s5
#graph for pass and fail
N=5
nd=np.arange(N)
width=0.3
fig=plt.figure()
ax=fig.add_subplot(111)
l=[s1,s2,s3,s4,s5]
r1=ax.barh(nd+width,l,width,color='orange')
l1=[f1,f2,f3,f4,f5]
r2=ax.barh(nd+width*2,l1,width,color='magenta')
ax.set_xlabel("No. of students")
ax.set_yticks(nd+width)
ax.set_yticklabels(('2011','2012','2013','2014','2015'))
ax.legend((r1[0],r2[0]),('Pass in Physics','Fail in Physics'))

def al(r):
  for i in r:
    h=i.get_y()+i.get_height()
    w=i.get_x()+i.get_width()
    ax.text(i.get_x()+i.get_width()/2,1.05*h,'%d'%int(w),ha='left',va='top')
al(r1);al(r2)
plt.show()


s1=s2=s3=s4=s5=n=0
#pass in chem
for a,b,c,d,e in zip(c1,c2,c3,c4,c5):
  if a >=40:
    s1+=1
  if b >=40 :
    s2+=1
  if c >=40 :
    s3+=1
  if d >=40:
    s4+=1
  if e >=40 :
    s5+=1
  n+=1
  
#fail
f1=n-s1;f2=n-s2;f3=n-s3;f4=n-s4;f5=n-s5
#graph for pass and fail
N=5
nd=np.arange(N)
width=0.3
fig=plt.figure()
ax=fig.add_subplot(111)
l=[s1,s2,s3,s4,s5]
r1=ax.barh(nd+width,l,width,color='yellow')
l1=[f1,f2,f3,f4,f5]
r2=ax.barh(nd+width*2,l1,width,color='red')
ax.set_xlabel("No. of students")
ax.set_yticks(nd+width)
ax.set_yticklabels(('2011','2012','2013','2014','2015'))
ax.legend((r1[0],r2[0]),('Pass in Chemistry','Fail in Chemistry'))

def al(r):
  for i in r:
    h=i.get_y()+i.get_height()
    w=i.get_x()+i.get_width()
    ax.text(i.get_x()+i.get_width()/2,1.05*h,'%d'%int(w),ha='left',va='top')
al(r1);al(r2)
plt.show()

s1=s2=s3=s4=s5=n=0
#pass 
for a,b,c,d,e in zip(m1,m2,m3,m4,m5):
  if a >=40:
    s1+=1
  if b >=40 :
    s2+=1
  if c >=40 :
    s3+=1
  if d >=40:
    s4+=1
  if e >=40 :
    s5+=1
  n+=1
  
#fail
f1=n-s1;f2=n-s2;f3=n-s3;f4=n-s4;f5=n-s5
#graph for pass and fail
N=5
nd=np.arange(N)
width=0.3
fig=plt.figure()
ax=fig.add_subplot(111)
l=[s1,s2,s3,s4,s5]
r1=ax.barh(nd+width,l,width,color='cyan')
l1=[f1,f2,f3,f4,f5]
r2=ax.barh(nd+width*2,l1,width,color='red')
ax.set_xlabel("No. of students")
ax.set_yticks(nd+width)
ax.set_yticklabels(('2011','2012','2013','2014','2015'))
ax.legend((r1[0],r2[0]),('Pass in Maths','Fail in Maths'))

def al(r):
  for i in r:
    h=i.get_y()+i.get_height()
    w=i.get_x()+i.get_width()
    ax.text(i.get_x()+i.get_width()/2,1.05*h,'%d'%int(w),ha='left',va='top')
al(r1);al(r2)
plt.show()

#hindi
N=5
#nd=np.arange(N)
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
plt.hist(l1,histtype='stepfilled',bins=[2011,2012,2013,2014,2015])


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
#plt.hist(l1,histtype='stepfilled',bins=[2011,2012,2013,2014,2015])
r4=ax.bar(nd+width*3,l1,width,color='c')
s1=s2=s3=s4=s5=n=0
#2nd div
for a,b,c,d,e in zip(h1,h2,h3,h4,h5):
  if a >=50 and a<60:
    s1+=1
  if b >=50 and b<60:
    s2+=1
  if c >=50 and c<60:
    s3+=1
  if d >=50 and d<60:
    s4+=1
  if e >=50 and e<60:
    s5+=1
l1=[s1,s2,s3,s4,s5]
r3=ax.bar(nd+width*2,l1,width,color='y')
s1=s2=s3=s4=s5=n=0
#1st div
for a,b,c,d,e in zip(h1,h2,h3,h4,h5):
  if a >=60 and a<75:
    s1+=1
  if b >=60 and b<75:
    s2+=1
  if c >=60 and c<75:
    s3+=1
  if d >=60 and d<75:
    s4+=1
  if e >=60 and e<75:
    s5+=1
l1=[s1,s2,s3,s4,s5]
r2=ax.bar(nd+width,l1,width,color='r')
s1=s2=s3=s4=s5=n=0
#distinction
for a,b,c,d,e in zip(h1,h2,h3,h4,h5):
  if a >=75:
    s1+=1
  if b >=75:
    s2+=1
  if c >=75:
    s3+=1
  if d >=75:
    s4+=1
  if e >=75:
    s5+=1

l=[s1,s2,s3,s4,s5]
r1=ax.bar(nd,l,width,color='orange')

ax.set_ylabel("No. of students-hindi")
ax.set_xticks(nd+width)
ax.set_xticklabels(('2011','2012','2013','2014','2015'))
ax.legend((r1[0],r2[0],r3[0],r4[0]),('Distinction','First Div','Second Div','Third Div'))

def al(r):
  for i in r:
    h=i.get_height()
    ax.text(i.get_x()+i.get_width()/2.,1.05*h,'%d'%int(h),ha='center',va='bottom')
al(r4);al(r3);al(r2);al(r1)
plt.show()

#english
N=5
nd=np.arange(N)
width=0.18
fig=plt.figure()
ax=fig.add_subplot(111)
s1=s2=s3=s4=s5=n=0
#3rd div 
for a,b,c,d,e in zip(e1,e2,e3,e4,e5):
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
r4=ax.bar(nd+width*3,l1,width,color='c')
s1=s2=s3=s4=s5=n=0
#2nd div
for a,b,c,d,e in zip(e1,e2,e3,e4,e5):
  if a >=50 and a<60:
    s1+=1
  if b >=50 and b<60:
    s2+=1
  if c >=50 and c<60:
    s3+=1
  if d >=50 and d<60:
    s4+=1
  if e >=50 and e<60:
    s5+=1
l1=[s1,s2,s3,s4,s5]
r3=ax.bar(nd+width*2,l1,width,color='r')
s1=s2=s3=s4=s5=n=0
#1st div
for a,b,c,d,e in zip(e1,e2,e3,e4,e5):
  if a >=60 and a<75:
    s1+=1
  if b >=60 and b<75:
    s2+=1
  if c >=60 and c<75:
    s3+=1
  if d >=60 and d<75:
    s4+=1
  if e >=60 and e<75:
    s5+=1
l1=[s1,s2,s3,s4,s5]
r2=ax.bar(nd+width,l1,width,color='g')
s1=s2=s3=s4=s5=n=0
#distinction
for a,b,c,d,e in zip(e1,e2,e3,e4,e5):
  if a >=75:
    s1+=1
  if b >=75:
    s2+=1
  if c >=75:
    s3+=1
  if d >=75:
    s4+=1
  if e >=75:
    s5+=1

l=[s1,s2,s3,s4,s5]
r1=ax.bar(nd,l,width,color='k')

ax.set_ylabel("No. of students-English")
ax.set_xticks(nd+width)
ax.set_xticklabels(('2011','2012','2013','2014','2015'))
ax.legend((r1[0],r2[0],r3[0],r4[0]),('Distinction','First Div','Second Div','Third Div'))

def al(r):
  for i in r:
    h=i.get_height()
    ax.text(i.get_x()+i.get_width()/2.,1.05*h,'%d'%int(h),ha='center',va='bottom')
al(r4);al(r3);al(r2);al(r1)
plt.show()

#physics
N=5
nd=np.arange(N)
width=0.18
fig=plt.figure()
ax=fig.add_subplot(111)
s1=s2=s3=s4=s5=n=0
#3rd div 
for a,b,c,d,e in zip(p1,p2,p3,p4,p5):
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
r4=ax.bar(nd+width*3,l1,width,color='m')
s1=s2=s3=s4=s5=n=0
#2nd div
for a,b,c,d,e in zip(p1,p2,p3,p4,p5):
  if a >=50 and a<60:
    s1+=1
  if b >=50 and b<60:
    s2+=1
  if c >=50 and c<60:
    s3+=1
  if d >=50 and d<60:
    s4+=1
  if e >=50 and e<60:
    s5+=1
l1=[s1,s2,s3,s4,s5]
r3=ax.bar(nd+width*2,l1,width,color='y')
s1=s2=s3=s4=s5=n=0
#1st div
for a,b,c,d,e in zip(p1,p2,p3,p4,p5):
  if a >=60 and a<75:
    s1+=1
  if b >=60 and b<75:
    s2+=1
  if c >=60 and c<75:
    s3+=1
  if d >=60 and d<75:
    s4+=1
  if e >=60 and e<75:
    s5+=1
l1=[s1,s2,s3,s4,s5]
r2=ax.bar(nd+width,l1,width,color='b')
s1=s2=s3=s4=s5=n=0
#distinction
for a,b,c,d,e in zip(p1,p2,p3,p4,p5):
  if a >=75:
    s1+=1
  if b >=75:
    s2+=1
  if c >=75:
    s3+=1
  if d >=75:
    s4+=1
  if e >=75:
    s5+=1

l=[s1,s2,s3,s4,s5]
r1=ax.bar(nd,l,width,color='g')

ax.set_ylabel("No. of students-Physics")
ax.set_xticks(nd+width)
ax.set_xticklabels(('2011','2012','2013','2014','2015'))
ax.legend((r1[0],r2[0],r3[0],r4[0]),('Distinction','First Div','Second Div','Third Div'))

def al(r):
  for i in r:
    h=i.get_height()
    ax.text(i.get_x()+i.get_width()/2.,1.05*h,'%d'%int(h),ha='center',va='bottom')
al(r4);al(r3);al(r2);al(r1)
plt.show()


#chemsitry
N=5
nd=np.arange(N)
width=0.18
fig=plt.figure()
ax=fig.add_subplot(111)
s1=s2=s3=s4=s5=n=0
#3rd div 
for a,b,c,d,e in zip(c1,c2,c3,c4,c5):
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
r4=ax.bar(nd+width*3,l1,width,color='b')
s1=s2=s3=s4=s5=n=0
#2nd div
for a,b,c,d,e in zip(c1,c2,c3,c4,c5):
  if a >=50 and a<60:
    s1+=1
  if b >=50 and b<60:
    s2+=1
  if c >=50 and c<60:
    s3+=1
  if d >=50 and d<60:
    s4+=1
  if e >=50 and e<60:
    s5+=1
l1=[s1,s2,s3,s4,s5]
r3=ax.bar(nd+width*2,l1,width,color='y')
s1=s2=s3=s4=s5=n=0
#1st div
for a,b,c,d,e in zip(c1,c2,c3,c4,c5):
  if a >=60 and a<75:
    s1+=1
  if b >=60 and b<75:
    s2+=1
  if c >=60 and c<75:
    s3+=1
  if d >=60 and d<75:
    s4+=1
  if e >=60 and e<75:
    s5+=1
l1=[s1,s2,s3,s4,s5]
r2=ax.bar(nd+width,l1,width,color='black')
s1=s2=s3=s4=s5=n=0
#distinction
for a,b,c,d,e in zip(c1,c2,c3,c4,c5):
  if a >=75:
    s1+=1
  if b >=75:
    s2+=1
  if c >=75:
    s3+=1
  if d >=75:
    s4+=1
  if e >=75:
    s5+=1

l=[s1,s2,s3,s4,s5]
r1=ax.bar(nd,l,width,color='r')

ax.set_ylabel("No. of students-Chemistry")
ax.set_xticks(nd+width)
ax.set_xticklabels(('2011','2012','2013','2014','2015'))
ax.legend((r1[0],r2[0],r3[0],r4[0]),('Distinction','First Div','Second Div','Third Div'))

def al(r):
  for i in r:
    h=i.get_height()
    ax.text(i.get_x()+i.get_width()/2.,1.05*h,'%d'%int(h),ha='center',va='bottom')
al(r4);al(r3);al(r2);al(r1)
plt.show()


#biology
N=5
nd=np.arange(N)
width=0.18
fig=plt.figure()
s1=s2=s3=s4=s5=n=0
ax=fig.add_subplot(111)
#3rd div 
for a,b,c,d,e in zip(b1,b2,b3,b4,b5):
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
r4=ax.bar(nd+width*3,l1,width,color='orange')
s1=s2=s3=s4=s5=n=0
#2nd div
for a,b,c,d,e in zip(b1,b2,b3,b4,b5):
  if a >=50 and a<60:
    s1+=1
  if b >=50 and b<60:
    s2+=1
  if c >=50 and c<60:
    s3+=1
  if d >=50 and d<60:
    s4+=1
  if e >=50 and e<60:
    s5+=1
l1=[s1,s2,s3,s4,s5]
r3=ax.bar(nd+width*2,l1,width,color='r')
s1=s2=s3=s4=s5=n=0
#1st div
for a,b,c,d,e in zip(b1,b2,b3,b4,b5):
  if a >=60 and a<75:
    s1+=1
  if b >=60 and b<75:
    s2+=1
  if c >=60 and c<75:
    s3+=1
  if d >=60 and d<75:
    s4+=1
  if e >=60 and e<75:
    s5+=1
l1=[s1,s2,s3,s4,s5]
r2=ax.bar(nd+width,l1,width,color='magenta')
s1=s2=s3=s4=s5=n=0
#distinction
for a,b,c,d,e in zip(b1,b2,b3,b4,b5):
  if a >=75:
    s1+=1
  if b >=75:
    s2+=1
  if c >=75:
    s3+=1
  if d >=75:
    s4+=1
  if e >=75:
    s5+=1

l=[s1,s2,s3,s4,s5]
r1=ax.bar(nd,l,width,color='yellow')

ax.set_ylabel("No. of students-Biology")
ax.set_xticks(nd+width)
ax.set_xticklabels(('2011','2012','2013','2014','2015'))
ax.legend((r1[0],r2[0],r3[0],r4[0]),('Distinction','First Div','Second Div','Third Div'))

def al(r):
  for i in r:
    h=i.get_height()
    ax.text(i.get_x()+i.get_width()/2.,1.05*h,'%d'%int(h),ha='center',va='bottom')
al(r4);al(r3);al(r2);al(r1)
plt.show()

N=5
nd=np.arange(N)
width=0.18
fig=plt.figure()
ax=fig.add_subplot(111)
s1=s2=s3=s4=s5=n=0
#3rd div 
for a,b,c,d,e in zip(m1,m2,m3,m4,m5):
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
r4=ax.bar(nd+width*3,l1,width,color='b')
s1=s2=s3=s4=s5=n=0
#2nd div
for a,b,c,d,e in zip(m1,m2,m3,m4,m5):
  if a >=50 and a<60:
    s1+=1
  if b >=50 and b<60:
    s2+=1
  if c >=50 and c<60:
    s3+=1
  if d >=50 and d<60:
    s4+=1
  if e >=50 and e<60:
    s5+=1
l1=[s1,s2,s3,s4,s5]
r3=ax.bar(nd+width*2,l1,width,color='g')
s1=s2=s3=s4=s5=n=0
#1st div
for a,b,c,d,e in zip(m1,m2,m3,m4,m5):
  if a >=60 and a<75:
    s1+=1
  if b >=60 and b<75:
    s2+=1
  if c >=60 and c<75:
    s3+=1
  if d >=60 and d<75:
    s4+=1
  if e >=60 and e<75:
    s5+=1
l1=[s1,s2,s3,s4,s5]
r2=ax.bar(nd+width,l1,width,color='red')
s1=s2=s3=s4=s5=n=0
#distinction
for a,b,c,d,e in zip(m1,m2,m3,m4,m5):
  if a >=75:
    s1+=1
  if b >=75:
    s2+=1
  if c >=75:
    s3+=1
  if d >=75:
    s4+=1
  if e >=75:
    s5+=1

l=[s1,s2,s3,s4,s5]
r1=ax.bar(nd,l,width,color='cyan')

ax.set_ylabel("No. of students-maths")
ax.set_xticks(nd+width)
ax.set_xticklabels(('2011','2012','2013','2014','2015'))
ax.legend((r1[0],r2[0],r3[0],r4[0]),('Distinction','First Div','Second Div','Third Div'))

def al(r):
  for i in r:
    h=i.get_height()
    ax.text(i.get_x()+i.get_width()/2.,1.05*h,'%d'%int(h),ha='center',va='bottom')
al(r4);al(r3);al(r2);al(r1)
plt.show()

s1=s2=s3=s4=s5=n=0
#avg of maths
for a,b,c,d,e in zip(m1,m2,m3,m4,m5):
    s1+=a
    s2+=b
    s3+=c
    s4+=d
    s5+=e;n+=1
s1=s1/n
s2=s2/n
s3=s3/n
s4=s4/n
s5=s5/n


N=5
nd=np.arange(N)
width=0.1

fig=plt.figure()
ax=fig.add_subplot(111)
l=[s1,s2,s3,s4,s5]
r1=ax.bar(nd,l,width,color='r')
s1=s2=s3=s4=s5=n=0
#avg of physics
for a,b,c,d,e in zip(p1,p2,p3,p4,p5):
    s1+=a
    s2+=b
    s3+=c
    s4+=d
    s5+=e;n+=1
s1=s1/n
s2=s2/n
s3=s3/n
s4=s4/n
s5=s5/n
print(s1,s2,s3,s4,s5)
l=[s1,s2,s3,s4,s5]
r2=ax.bar(nd+width,l,width,color='g')
s1=s2=s3=s4=s5=n=0
#avg of chemistry
for a,b,c,d,e in zip(c1,c2,c3,c4,c5):
    s1+=a
    s2+=b
    s3+=c
    s4+=d
    s5+=e;n+=1
s1=s1/n
s2=s2/n
s3=s3/n
s4=s4/n
s5=s5/n
l=[s1,s2,s3,s4,s5]
r3=ax.bar(nd+width*2,l,width,color='b')
s1=s2=s3=s4=s5=n=0
#avg of biology
for a,b,c,d,e in zip(b1,b2,b3,b4,b5):
    s1+=a
    s2+=b
    s3+=c
    s4+=d
    s5+=e;n+=1
s1=s1/n
s2=s2/n
s3=s3/n
s4=s4/n
s5=s5/n

l=[s1,s2,s3,s4,s5]
r4=ax.bar(nd+width*3,l,width,color='orange')
s1=s2=s3=s4=s5=n=0
#avg of english
for a,b,c,d,e in zip(e1,e2,e3,e4,e5):
    s1+=a
    s2+=b
    s3+=c
    s4+=d
    s5+=e;n+=1
s1=s1/n
s2=s2/n
s3=s3/n
s4=s4/n
s5=s5/n

l=[s1,s2,s3,s4,s5]
r5=ax.bar(nd+width*4,l,width,color='magenta')

s1=s2=s3=s4=s5=n=0
#avg of hindi
for a,b,c,d,e in zip(h1,h2,h3,h4,h5):
    s1+=a
    s2+=b
    s3+=c
    s4+=d
    s5+=e;n+=1
s1=s1/n
s2=s2/n
s3=s3/n
s4=s4/n
s5=s5/n

l=[s1,s2,s3,s4,s5]
r6=ax.bar(nd+width*5,l,width,color='yellow')

ax.set_ylabel("Marks")
ax.set_xticks(nd+width)
ax.set_xticklabels(('2011','2012','2013','2014','2015'))
ax.legend((r1[0],r2[0],r3[0],r4[0],r5[0],r6[0]),('M','P','C','B','E','H'))

def al(r):
  for i in r:
    h=i.get_height()
    ax.text(i.get_x()+i.get_width()/2.,1.05*h,'%d'%int(h),ha='center',va='bottom')
al(r1);al(r2);al(r3);al(r4);al(r5);al(r6)
plt.show()

