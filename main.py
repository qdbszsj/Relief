import numpy as np
import pandas as pd
dataset=pd.read_csv('/home/parker/watermelonData/watermelon_3.csv', delimiter=",")
del dataset['编号']
print(dataset)
attributeMap={}
attributeMap['浅白']=0
attributeMap['青绿']=0.5
attributeMap['乌黑']=1
attributeMap['蜷缩']=0
attributeMap['稍蜷']=0.5
attributeMap['硬挺']=1
attributeMap['沉闷']=0
attributeMap['浊响']=0.5
attributeMap['清脆']=1
attributeMap['模糊']=0
attributeMap['稍糊']=0.5
attributeMap['清晰']=1
attributeMap['凹陷']=0
attributeMap['稍凹']=0.5
attributeMap['平坦']=1
attributeMap['硬滑']=0
attributeMap['软粘']=1
attributeMap['否']=0
attributeMap['是']=1
data=dataset.values


m,n=np.shape(data)
for i in range(m):
    for j in range(n):
        if data[i,j] in attributeMap:
            data[i,j]=attributeMap[data[i,j]]
        else: data[i,j]=round(data[i,j],3)

X=data[:,:-1]
y=data[:,-1]
m,n=np.shape(X)
# print(X,y)
near=np.zeros((m,2))#near[i,0] is nearHit, near[i,1] is nearMiss
# print(near)

def distance(x1,x2):
    return sum((x1-x2)**2)

for i in range(m):
    hitDistance=99999 #init as INF
    missDistance=99999
    for j in range(m):
        if j==i:continue
        curDistance=distance(X[i],X[j])
        if y[i]==y[j] and curDistance<hitDistance:
            hitDistance=curDistance
            near[i,0]=j
        if y[i]!=y[j] and curDistance<missDistance:
            missDistance=curDistance
            near[i,1]=j

#P250--(11.3)
relief=np.zeros(n)
for j in range(n):
    for i in range(m):
        relief[j]+=(X[i,j]-X[int(near[i,1]),j])**2-(X[i,j]-X[int(near[i,0]),j])**2
print(relief)