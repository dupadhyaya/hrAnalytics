# -*- coding: utf-8 -*-
#Created by DU 
#Topic : Create Data Frame
#%%%#libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import pydataset as data
import string
import random
#%%%  Fake DF
df1A = pd.DataFrame(np.random.rand(50,5).round(2))  #5 cols, 50 rows
df1A.head()
df1A.index = pd.date_range('1/1/2023', periods=len(df1A), freq='M')
df1A.head()

string.ascii_uppercase , string.ascii_lowercase 
df1A.shape
rows, cols = 52, 5
df1B = pd.DataFrame(np.random.randn(rows, cols).round(2), columns = ['c' + str(i) for i in range(cols)] , index = list((string.ascii_uppercase + string.ascii_lowercase)[0:rows]))
df1B['group'] = [random.choice('abcde') for _ in range(rows)]
df1B

#%%% from dictionary
df2A = pd.DataFrame.from_dict({'R0':{'C1':0, 'C2':'A'}, 'R1':{'C1':10, 'C2':'B'}}, orient='index')
df2A
df2B = pd.DataFrame.from_dict({'R0':[1,2,3], 'R1':[5,6,7]}, orient='index', columns=['C3','C4','C5'])
df2B
#%%% create data frame
n=50
empID = random.sample(range(100,300),n)
empID
depts = ['HR','Marketing', 'Finance', 'Operations']
name = pd.Series(['Employee' + str(i) for i in range(1,n+1)])
name
age = np.random.randint(low=23, high=50, size=n)
age
gender = random.choices(['M','F'], weights =(.7,.3), k=n)
dept = random.choices(depts, k=n)
pd.DataFrame({'empID':empID, 'name':name, 'gender':gender, 'dept':dept, 'age':age, 'salary':salary})
salary = np.random.randint(low=10000, high=100000, size=n)
appraisal = np.random.normal(loc=7,scale=1,size=n).round(n)
appraisal
sDate = '2020/01/01'; eDate ='2023/01/01'
sampleDates = pd.date_range(sDate, eDate).to_series()
sampleDates
len(appraisal)
doj = sampleDates.sample(n, replace=False, random_state=100)
type(doj)
dojList = doj.tolist()
len(dojList)
myList1 = [empID, name, gender, dept, age, salary, appraisal, doj]
for i in myList1: print(len(i))
df3 = pd.DataFrame({'empID':empID, 'name':name, 'gender':gender, 'dept':dept, 'age':age, 'salary':salary, 'appraisal':appraisal, 'doj':dojList})
df3

df3['raiseLY'] = [random.choice('YN')  for _ in range(len(df3))]
df3['married'] = [random.choice([True,False, np.NaN])  for _ in range(len(df3))]
df3[['raiseLY','married']]
df3['distOffice'] = np.random.randint(low=3, high=25, size=n)
rRows = np.random.randint(low=0, high=n, size=round(n/4))
rRows
df3.loc[rRows, 'distOffice'] = np.nan
df3.isnull().sum()

cities = ('Gurugram', 'Noida','Delhi', 'Mumbai', 'Bengaluru','Chennai', 'Kolkatta')
random.sample(cities, counts=[4,13,2,14,2,12,4], k=n)
df3['homeTown'] = np.random.choice(cities, size=50, replace=True)
df3['homeTown'].tolist()

df3
df3.describe()
df3.info()
df3.dtypes
df3.columns
df3.columns.tolist()  #list
df3.columns.values  #array
cols1 = ['gender','dept','raiseLY','homeTown']
for col in cols1:    df3[col] = df3[col].astype('category')

#%%% columns
#change colnames
#df = df.rename(columns ={'old':'new'})
#df.columns =['new1','new2']

#select cols
df3['name']  #col to series
df3.name
df3[['name']]  #col as DF
df3[['name', 'dept']]  #2+ cols
df3[['name', 'dept','empID']]#order of cols
df3[df3.columns[[1,4,3]]] # cols by position
df3[df3.columns[-1]] # last cols by position
df3[df3.columns[:-1]] # ignore last cols by position

#df1
df1B.loc[::]
df1B.loc[:,:]
df1B.loc[:,'c0':'c2']
df1B.iloc[1:10,0:2]
df1B.iloc[[3,4,2],[0,3,5]]


#drop
df3.drop('daysServed', axis=1, inplace=False)  #one col by name
df3.drop(['dept','daysServed'], axis=1, inplace=False) #2 cols by name
df3.drop(df3.columns[3:11], axis=1, inplace=False) # 3 to 11
df3.drop(df3.columns[-1:], axis=1, inplace=False)  #last
#values to list
df3['age'].tolist()
df3['age'].idxmin()   #which row has min age
df3.loc[1:10, 'age']

#others-advanced
df3['age'].pct_change(periods=4)

df3.isna().sum()
df3['distOffice'].isnull()
df3['distOffice'].notnull()
df3['married'].count()   #count non NA


df3['distOffice'].fillna(100)
df3['married'].fillna('NK')

#%%% rows
df1B.head()
df1B.index.tolist()  #list
df1B.index.values   #array

#add rows
df1B.append(df1B).count()
#drop rows
df1B.drop('A', inplace=False).head()
df1B.drop(['A','B'], inplace=False).head()
idx = df3[df3['age'] > 30]
idx
df3[idx,]

#slice
df1B[:]
df1B[0:3]
df1B.head(4)
df1B[-1:]
df1B[::5]  #every 5th
df1B['A':'D']
df1B.iloc[4:6,:]
df1B.iloc[random.sample(range(len(df1B)),6),:]

#%%%% rows cols
df1B.iloc[1:5, 2:4]
df1B.iat[1, 2]  #particular cel position
df1B.loc['A':'C', 'c0']  #by label
df1B.xs('A')   #leave this

#%%%
df3.dtypes
df3.describe(include='all')
df3.shape
df3.ndim
df3.empty
df3.size
df3.values
df3.iteritems()
df3.iterrows()
for (name, series)  in df3.items():
    print('\n Variable' + str(name) + ' : 1st Employee Values : '+ str( series.iat[0]))
df3.columns
for (name, series)  in df3.iterrows():
    print('\n Home Town of Employee ' + str(name) + ' : is : '+ str(series.iat[11]))
#%%%
df3.sort_values(by='doj').filter(items=['doj', 'name'])
#%%%

#%%%   Queries
df3.columns
#total experience  : sysdate - doj = total
from datetime import datetime, date
datetime.today()
datetime.now()
dToday = datetime.strptime('2023/06/25', '%Y/%m/%d')
dToday
df3['daysServed'] = dToday - df3['doj']
df3['daysServed'].sum()
df3['daysServed'].max()
df3['daysServed'].min()

#groupby
df3.groupby('dept').agg({'daysServed': [np.sum, np.min, np.max]})
df3.groupby(['dept','gender']).agg({'daysServed': ['count', np.sum, np.min, np.max]}).reset_index()

#%%% emp serving > 1000 days
df3sc1 = ['empID', 'name','dept']
df3.loc[df3['daysServed'] > '1000 days',['empID','name', 'dept', 'daysServed']]
df3.loc[(df3['daysServed'] > '1000 days') & (df3['gender'] == 'F'),['empID','name', 'dept', 'daysServed', 'gender']]
#%%% is in dept
type(df3[df3['dept'].isin(['HR','Finance'])])
df3[df3['dept'].isin(['HR','Finance'])].filter(items=df3sc1)
df3[~df3['dept'].isin(['HR','Finance'])].filter(items=df3sc1)
df3[df3['dept'].str.contains('Fin|Mar')].filter(items=df3sc1)
df3[df3['dept'].str.contains('Fin|Mar')].filter(items=df3sc1).count()

#which rowid have salary > 75000
df3.columns.get_loc('salary')  #ser no of col salary
df3.iloc[:, 5]
np.where(df3['salary'] > 75000)
df3.iloc[np.where(df3['salary'] > 75000)].filter(items=['empID','dept', 'salary'])


#%%%duplicates
df3.duplicated()
df3.groupby(['gender','dept', 'age']).agg('count').reset_index()
df3[df3[['gender','age', 'dept']].duplicated(keep=False)][['name','age', 'gender','dept']].sort_values(by=['gender','dept','age'])
#keep first duplicate items
df3[df3[['gender','age', 'dept']].duplicated(keep='last')][['name','age', 'gender','dept']].sort_values(by=['gender','dept','age'])
df3.drop_duplicates(subset=['gender','age', 'dept'], inplace=False, keep='first')[['name','gender','age', 'dept']]
df3.drop_duplicates(subset=['dept'], inplace=False, keep='first')[['name','dept']]



#%%%% missing
df3.isnull().sum()
df3.notnull().sum()
df3.notnull().sum(axis=1)

df3.isna().sum()
df3.info()
np.where(df3['distOffice'].isnull())[0]
np.where(df3['married'].isnull())[0]
df3.isna().any(axis=1)
misRows = np.where(df3.isna().any(axis=1))[0] #all rows having even 1 col value missing
misRows
df3.loc[misRows, ['gender','married','distOffice']]
df3.loc[:,['gender', 'married','distOffice' ]]
df3.loc[:,['gender', 'married','distOffice' ]].fillna( method='pad')# fill fwd
df3[['gender','married','distOffice']].fillna(method='bfill')# fill back

#fill missing values with particular values
df3['distOffice'].mean()
df3['distOffice'].fillna(value = df3['distOffice'].mean(), inplace=False)
(df3['distOffice'].fillna(value = df3['distOffice'].mean(), inplace=False) == df3['distOffice'].mean()).sum()

#several imputing functions

#%%% reshape




#%%%% pivot


#%%% crosstab


#%%% groupby



#%%% graphs



#%%%%%%



#%%%%merge


