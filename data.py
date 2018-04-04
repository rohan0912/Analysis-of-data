import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

d=pd.read_excel("hsc1.xlsx")

y1=pd.read_excel("2011.xlsx");y1=y1[['English','Hindi','Physics','Chemistry','Maths','Biology']]
y2=pd.read_excel("2012.xlsx");y2=y2[['English','Hindi','Physics','Chemistry','Maths','Biology']]
y3=pd.read_excel("2013.xlsx");y3=y3[['English','Hindi','Physics','Chemistry','Maths','Biology']]
y4=pd.read_excel("2014.xlsx");y4=y4[['English','Hindi','Physics','Chemistry','Maths','Biology']]
y5=pd.read_excel("2015.xlsx");y5=y5[['English','Hindi','Physics','Chemistry','Maths','Biology']]
m1=list(y1.Maths)
m2=list(y2.Maths)
m3=list(y3.Maths)
m4=list(y4.Maths)
m5=list(y5.Maths)

p1=list(y1.Physics)
p2=list(y2.Physics)
p3=list(y3.Physics)
p4=list(y4.Physics)
p5=list(y5.Physics)

c1=list(y1.Chemistry)
c2=list(y2.Chemistry)
c3=list(y3.Chemistry)
c4=list(y4.Chemistry)
c5=list(y5.Chemistry)

e1=list(y1.English)
e2=list(y2.English)
e3=list(y3.English)
e4=list(y4.English)
e5=list(y5.English)

h1=list(y1.Hindi)
h2=list(y2.Hindi)
h3=list(y3.Hindi)
h4=list(y4.Hindi)
h5=list(y5.Hindi)

b1=list(y1.Biology)
b2=list(y2.Biology)
b3=list(y3.Biology)
b4=list(y4.Biology)
b5=list(y5.Biology)
