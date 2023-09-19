#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd 
import numpy as np 
import mysql.connector as sql
amount=0
payfor=0
payforlist=[]
amountlist=[]
while payfor!='-1':
    payfor=str(input('Pay for:'))
    payforlist.append(payfor)
    amount=float(input('Expense amount:'))
    amountlist.append(amount)
    
expenses=pd.Series(amountlist[:len(amountlist)-1],payforlist[:len(payforlist)-1])
print(expenses)


# In[21]:


print(expenses)


# amountlist.len

# In[ ]:





# In[26]:


import pandas as pd 
import numpy as np 
import mysql.connector as sql
amount=0
payforlist=[]
amountlist=[]
count=0
entries=float(input('How many entries for Expenses?'))
print('Enter NONE if no more entries are required')
while count<entries :
    payfor=str(input('Pay for:'))
    payforlist.append(payfor)
    amount=float(input('Expense amount:'))
    amountlist.append(amount)
    count+=1
expenses=pd.Series(amountlist,payforlist)
print(expenses)


# In[24]:


print(1)


# In[9]:


import pandas as pd
a=pd.Series([10.20,30,40])
print(a)


# In[14]:


len(a)


# In[30]:


import pandas as pd
import numpy as np 
abc=pd.read_csv('/Users/yash/Desktop/exp1.csv',names=['S.no','N','R'])
print(abc)


# In[10]:


import pandas as pd
a=pd.Series((1,2,3,4),[10,20,30,40])
print(a)
a[[10,20]]=1000
print(a)


# In[3]:


import numpy as np

print(np.linspace(1,20,5))


# In[11]:


print(a
     )


# In[13]:


a[20]=0
print(a)


# In[45]:


bb=pd.DataFrame({'Arnav':[10,20,30,40],'Moksha':[1,2,3,4],'Thanupa':[11,22,33,44],'Arjun':[111,222,333,444]},
                index=['Name','Age','Height','Weight'])
print(bb)


# In[46]:


bb[bb.Thanupa>20]


# In[47]:


bb['Arham']=[11,12,13,14]


# In[48]:


print(bb)


# In[49]:


bb.loc['Lname',:]=[11,2,3,4,5]


# In[50]:


print(bb)


# In[51]:


bb.at['hi']=10


# In[29]:


print(bb)


# In[30]:


bb.Arnav=[1,2,3,4,5,6666]
print(bb)


# In[ ]:





# In[101]:


print(bb)


# In[107]:


for (row,rowS) in bb.iterrows():
    print(rowS['Moksha'])
    print('---')


# In[113]:


bb.describe()


# In[114]:


bb.info()


# In[117]:


print(bb.head(n=3))


# In[128]:


bb.cumsum(axis=1)


# In[145]:


bb.count()


# In[146]:


grp= pd.DataFrame({'A':[28,19,47,38,29,38,474,0,48,18],
                   'B':[1,20,38,1,9,29,30,49,28,40],
                   'C':[28,39,18,40,2,40,28,40,658,3]})
print(grp)


# In[148]:


df=grp.groupby('A')


# In[149]:


df.groups


# In[151]:


df.get_group(38)


# In[156]:


df['B'].head()


# In[157]:


a=grp.groupby('C')
a.size()


# In[163]:


a.get_group(40).sum(1)


# In[166]:


len(bb)


# In[170]:


bb.Moksha.idxmax()


# In[172]:


print(bb.hist())


# In[173]:


bb


# In[179]:


i=0
for (a,b) in bb.iteritems():
    if (i<3):
        print(a)
        print(b)
        i=i+1


# In[181]:


bb.count(1)


# In[462]:


import matplotlib.pyplot as plt
plt.plot([10,20,30,40],'+',ls='-.',linewidth=10)
plt.figure(figsize=(900,100))
plt.grid()
plt.show()


# In[280]:


import numpy as np
x=np.arange(1,5)
plt.bar(x,[10,20,30,22],color=['k','r','g'],width=0.3,label='First')
plt.bar(x+0.25,[11,30,28,54],width=0.28,color=['b','g','c','m'],label='Second')
plt.legend(loc=1)
plt.xlim(-1,5)
plt.ylim(-5,100)
plt.xticks([1,2,4])
plt.show()


# In[257]:


print(x)


# In[306]:


print(bb)
bb.rename(index={'name':'Bye'},inplace=True)
bb.drop('Bye',inplace=True)


# In[344]:


plt.plot([1,2,3,4,5],[10,22,33,44,55]
         ,[1,1,22,33,44],'+',ls='--')
#plt.plot([1,2,3,4],[11,22,33,44],'c+',ls='--')
plt.xlim(1,6)
plt.xticks([1,2,3,4,5,6])
plt.show()


# In[ ]:





# #### plt.plot(bb.Moksha)

# In[351]:


bb.plot()


# In[370]:


bb.Moksha.plot()


# In[381]:


a=pd.Series([10,20,30,40],[1,2,3,4])
print(a)


# In[386]:


kk=pd.DataFrame([[10,20,30],[1,2,3],[5,6,6]],index=[11,22,33],columns=[19,29,39])
print(bb)


# In[391]:


bb.loc[:'height',:'Arjun']


# In[592]:


final=pd.Series([11,22,33,44],[1,2,3,4])
print(final)


# In[401]:


kk.drop(22)


# In[402]:


kk


# In[405]:


bb


# In[406]:


bb.set_index('Moksha',inplace=True)


# In[418]:


print(bb)
print(kk)

bb.rename(columns={'Thanupa':19,'Arjun':29,'Arham':39},inplace=True)
print(bb)


# In[420]:


bb.index.name=19


# In[436]:


print(bb)


# In[593]:


bb.rename(index={2.0:'hi',3.0:'by',4.0:'lol',2.0:'1gg'},inplace=True)


# In[598]:


bb.insert(loc=0,column='EY',value=[11,22,33,444])
print(bb)


# In[603]:


bb.axes[0]


# In[607]:


del bb['EY']


# In[608]:


print(bb)


# In[ ]:




