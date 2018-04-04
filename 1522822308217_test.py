import matplotlib.pyplot as pt
import pandas as pd
import numpy as np

d=pd.read_excel("C:\pythonprog\experiments\HSC_data.xlsx")
d1=pd.read_excel("C:\pythonprog\experiments\Book1.xlsx")
d2=pd.read_excel("C:\pythonprog\experiments\Book2.xlsx")
d3=pd.read_excel("C:\pythonprog\experiments\Book3.xlsx")
d4=pd.read_excel("C:\pythonprog\experiments\Book4.xlsx")
d5=pd.read_excel("C:\pythonprog\experiments\Book5.xlsx")

d1=d.head(50)
#d2=d.head(50)

#pt.plot(d["Seat No"],d["Biology"],color="red")
pt.plot(d1["Seat No"],d1["Biology"],color="blue",label="plot")
pt.legend()
pt.xlabel("Seat NO.",color="blue")
pt.ylabel("Biology marks",color="red")
pt.title("SEAT NO. vs BIOLOGY MARKS in 2011",color="green")
pt.show()

pt.bar(d1["Seat No"],d1["Chemistry"],color="Orange",label="bar")
pt.legend()
pt.xlabel("Seat NO.",color="blue")
pt.ylabel("Chemistry marks",color="red")
pt.title("SEAT NO. vs CHEMISTRY MARKS in 2011",color="green")
pt.show()

pt.barh(d1["Seat No"],d1["Maths"],color=["red","blue"],label="barh")
pt.legend()
pt.ylabel("Seat NO.",color="blue")
pt.xlabel("Maths marks",color="red")
pt.title("SEAT NO. vs MATHS MARKS in 2011",color="RED")
pt.show()

pt.plot(d1["Seat No"],d1["Physics"],color="green",label="plot")
pt.legend()
pt.xlabel("Seat NO.",color="blue")
pt.ylabel("Physics marks",color="red")
pt.title("SEAT NO. vs PHYSICS MARKS in 2011",color="RED")
pt.show()

pt.scatter(d1["Seat No"],d1["English"],color=["Blue","Green"],label="scatter")
pt.legend()
pt.xlabel("Seat NO.",color="blue")
pt.ylabel("English marks",color="red")
pt.title("SEAT NO. vs ENGLISH MARKS in 2011",color="RED")
pt.show()


fig=pt.figure()
fig.patch.set_facecolor("Lightgray")
graph=fig.add_subplot(1,2,1,facecolor="Lightgray")
x=len(d2[d2.English>80])
x1=len(d2[(d2.English>=60) & (d2.English<70)])
x2=len(d2[d2.English<60])
graph.pie([x,x1,x2],colors=['blue','green','red'],labels=['>80%','60%-70%','<60%'])
graph.set_title("MARKS IN ENGLISH SUBJECT  (2012)")

#fig=pt.figure()
#fig.patch.set_facecolor("Lightgray")
graph1=fig.add_subplot(1,2,2,facecolor="Lightgray")
x=len(d2[d2.Maths>80])
x1=len(d2[(d2.Maths>=60) & (d2.Maths<70)])
x2=len(d2[d2.Maths<60])
graph1.pie([x,x1,x2],colors=['blue','green','red'],labels=['>80%','60%-70%','<60%'])
graph1.set_title("MARKS IN MATHS SUBJECT")
pt.show()


fig=pt.figure()
fig.patch.set_facecolor("Lightgray")
graph=fig.add_subplot(1,1,1,facecolor="Lightgray")
y=len(d2[d2.Physics>80])
y1=len(d2[(d2.Physics>=60) & (d2.Physics<70)])
y2=len(d2[d2.Physics<60])
graph.pie([y,y1,y2],colors=['blue','green','red'],labels=['>80%','60%-70%','<60%'])
graph.set_title("MARKS IN Physics SUBJECT  (2012)")
pt.show()


a1=np.array(d1["Maths"])
b1=np.array(d1["English"])
c1=np.array(d1["Physics"])
p1=np.array(d1["Chemistry"])
e1=np.array(d1["Biology"])
r1=a1+b1+c1+p1+e1
di1=0
vg1=0
g1=0
p1=0
f1=0
for i in r1:
    if i>=400:
        di1+=1
    elif i>=300 and i<400:
        vg1+=1
    elif i>=225 and i<300:
        g1+=1
    elif i>=175 and i<225:
        p1+=1
    else:
        f1+=1
        
l1=[]
l1.append(di1)
l1.append(vg1)
l1.append(g1)
l1.append(p1)
l1.append(f1)

fig1=pt.figure()
fig1.patch.set_facecolor("WHITE")
graph1=fig1.add_subplot(1,1,1,facecolor="ORANGE")
graph1.pie(l1,colors=['blue','green','red','yellow','orange'],labels=['Distinction','Very good','Good','Pass','Fail'])
graph1.set_title("RESULT IN YEAR 2011")
pt.show()


a2=np.array(d2["Maths"])
b2=np.array(d2["English"])
c2=np.array(d2["Physics"])
p2=np.array(d2["Chemistry"])
e2=np.array(d2["Biology"])
r2=a2+b2+c2+p2+e2
di2=0
vg2=0
g2=0
p2=0
f2=0
for i in r2:
    if i>=400:
        di2+=1
    elif i>=300 and i<400:
        vg2+=1
    elif i>=225 and i<300:
        g2+=1
    elif i>=175 and i<225:
        p2+=1
    else:
        f2+=1
        
l2=[]
l2.append(di2)
l2.append(vg2)
l2.append(g2)
l2.append(p2)
l2.append(f2)
fig2=pt.figure()
fig2.patch.set_facecolor("WHITE")
graph2=fig2.add_subplot(1,1,1,facecolor="ORANGE")
graph2.pie(l2,colors=['green','blue','gray','yellow','red'],labels=['Distinction','Very good','Good','Pass','Fail'])
graph2.set_title("RESULT IN YEAR 2012")
pt.show()

a3=np.array(d3["Maths"])
b3=np.array(d3["English"])
c3=np.array(d3["Physics"])
p3=np.array(d3["Chemistry"])
e3=np.array(d3["Biology"])
r3=a3+b3+c3+p3+e3
l3=[]
di3=0
vg3=0
g3=0
p3=0
f3=0
for i in r3:
    if i>=400:
        di3+=1
    elif i>=300 and i<400:
        vg3+=1
    elif i>=225 and i<300:
        g3+=1
    elif i>=175 and i<225:
        p3+=1
    else:
        f3+=1
        
l3.append(di3)
l3.append(vg3)
l3.append(g3)
l3.append(p3)
l3.append(f3)
fig3=pt.figure()
fig3.patch.set_facecolor("lightgray")
graph3=fig3.add_subplot(1,1,1,facecolor="ORANGE")
graph3.pie(l3,colors=['green','cyan','blue','pink','red'],labels=['Distinction','Very good','Good','Pass','Fail'])
graph3.set_title("RESULT IN YEAR 2013")
pt.show()


a4=np.array(d5["Maths"])
b4=np.array(d5["English"])
c4=np.array(d5["Physics"])
p4=np.array(d5["Chemistry"])
e4=np.array(d5["Biology"])
r4=a4+b4+c4+p4+e4
l4=[]
di4=0
vg4=0
g4=0
p4=0
f4=0
for i in r4:
    if i>=400:
        di4+=1
    elif i>=300 and i<400:
        vg4+=1
    elif i>=225 and i<300:
        g4+=1
    elif i>=175 and i<225:
        p4+=1
    else:
        f4+=1
        
l4.append(di4)
l4.append(vg4)
l4.append(g4)
l4.append(p4)
l4.append(f4)
fig4=pt.figure()
fig4.patch.set_facecolor("lightgray")
graph4=fig4.add_subplot(1,1,1,facecolor="ORANGE")
graph4.pie(l4,colors=['purple','yellow','blue','orange','red'],labels=['Distinction','Very good','Good','Pass','Fail'])
graph4.set_title("RESULT IN YEAR 2014")
pt.show()


a5=np.array(d5["Maths"])
b5=np.array(d5["English"])
c5=np.array(d5["Physics"])
p5=np.array(d5["Chemistry"])
e5=np.array(d5["Biology"])
r5=a5+b5+c5+p5+e5
l5=[]
di5=0
vg5=0
g5=0
p5=0
f5=0
for i in r5:
    if i>=400:
        di5+=1
    elif i>=300 and i<400:
        vg5+=1
    elif i>=225 and i<300:
        g5+=1
    elif i>=175 and i<225:
        p5+=1
    else:
        f5+=1
        
l5.append(di5)
l5.append(vg5)
l5.append(g5)
l5.append(p5)
l5.append(f5)
fig5=pt.figure()
fig5.patch.set_facecolor("lightgray")
graph5=fig5.add_subplot(1,1,1,facecolor="ORANGE")
graph5.pie(l4,colors=['yellow','green','blue','pink','brown'],labels=['Distinction','Very good','Good','Pass','Fail'])
graph5.set_title("RESULT IN YEAR 2015")
pt.show()
'''x=[1,2,3,4,5]
y=[5,-2,4,1,3]

pt.plot(x,y)
pt.show()

'''
