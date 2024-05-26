import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
s=pd.read_csv('2024-05-26.csv')
data=s.iloc[:,0:1].values
data2=s.iloc[:,1:2].values

def to1d(g):
    o = []
    l=[]
    for i in g:
        for j in i:
            o.append(j)


    return(o)

data=to1d(data)
data2=to1d(data2)

data3={'names':data,'time':data2}
df=pd.DataFrame(data3)

#print(df)

i=df.drop_duplicates(subset='names',keep='first')
#print(i)
i.to_csv('output.csv')
zz=pd.read_csv('output.csv')
print(zz.head())


