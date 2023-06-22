# -*- coding: utf-8 -*-
#Created by DU 
#Topic : General Practise on Pandas and Matplotlib
#%%%
#libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from matplotlib.pyplot import style
import seaborn as sns
import datetime as dt
from datetime import timedelta
from pydataset import data
import random
#%%% Options
pd.set_option('display.max_rows', 20)
pd.set_option('display.max_columns', 11)
pd.set_option('display.width', 1000)
#%%%
data('mtcars').head
mt = data('mtcars')
mt.head()
mt.describe()
mt.shape
mt.columns
mt.values
mt.dtypes
mt.index



catCols = ['am','vs','gear','cyl','carb']
numCols = ['mpg','disp', 'hp', 'drat', 'qsec']
catCols
numCols
mt[numCols]
mt[catCols] = mt[catCols].astype('category')
mt[catCols]
mt.describe(include='all')
#%%%dates & carnames
mt['carnames'] = mt.index
def generate_dates(start, end, n, seed=1, replace=False):
    dates = pd.date_range(start, end).to_series()
    return dates.sample(n, replace=replace, random_state=seed)
sDate = dt.date(2020,1,1)
eDate = dt.date.today()

dom = generate_dates(start=sDate, end=eDate, n=32, seed=22)
dom.tolist()
len(dom)
type(dom.tolist())
mt['dom'] = dom.tolist()
mt['dom'] = pd.to_datetime(mt['dom']).dt.normalize()  #only date
mt.head()
mt.columns
mt.dtypes
#%%%
mt.axes
mt.shape
mt.isna().sum(axis=1)
mt.isna().sum(axis=0)

mt.iloc[3:5,4:10]
mt.count(axis=1)
mt.count(axis=0)
mt.kurtosis()
mt.skew()
mt.max()
mt.mean()
mt.quantile([0., .5, .75, 1])
mt.rank()
mt.mad()
mt.aggregate(['mean', 'max'])
#apply, transform, applymap, 
mt[numCols].gt(10)
mt.cov()
mt.corr()
mt.std()
mt.var()
mt.nunique()
mt.duplicated()

mt[['am','vs']]
mt[['am','vs']].duplicated()

#%%% indexing 
mt.axes
mt.empty
mt.ndim
mt.size #row*col 
mt[['mpg','wt']].rank()
mt.sort_index().index
mt.index

#%%% sort, functions
mt.sort_values(by='gear')
mt.sort_values(by=['am', 'gear']).head()
mt.sort_values(by=['am', 'gear'], ascending=[True, False]).head()
mt.nlargest(4, columns='hp')
mt.nlargest(6, columns=['mpg','hp'])
mt.nsmallest(4, columns='hp')
mt.nsmallest(6, columns=['mpg','hp'])
mt = mt.sort_values(by='mpg')
mt.head()
mt[sorted(mt.columns)]
mt2 = mt.sort_index(axis=1)
mt2.truncate(before='hp', after='vs', axis='columns')
mt2B = mt.sort_index(axis=0)
mt2B
mt2B.truncate(before='Camaro Z28', after='Toyota Corolla', axis='rows')
mt.fillna(100)
mt.pivot(index=['am','vs','hp'], columns=['gear','carb'], values='mpg')
#%%%
mt.sort_values(by='wt').plot(x='wt',y='mpg')
mt.plot.bar(x='gear')
#%%% maths
mt[numCols].abs
mt[numCols].add(100)
mt[numCols].count()
mt[numCols].cummax()
mt[numCols].max()
mt[numCols].sum()
mt[numCols].cumsum()
mt[numCols].diff()  #within col : R1-R2
mt[numCols].head()  #within col : R1-R2


#%%%
mt.to_dict()
mt.to_clipboard()
mt.to_excel()
mt.to_csv()
#%%%% Working with row and col position and values
mt.index
mt.columns
mt
#get and set values
mt.at['Fiat 128','mpg']  #df.at['row','col'] #labels
mt.loc['Fiat 128','mpg']  #same as above
mt['mpg'].at['Fiat 128']  #same as above
mt.iat[30,0]
mt.iloc[30,0]
#mt.ix  #not avl now
#slicing & setting----
mt.loc['Mazda RX4':'Fiat 128', 'mpg':'hp']
mt.iloc[28:30,0:5]  #cross section
mt.iloc[:5,11:]  #cross section
mt.iloc[5,:]  #row as series
mt.iloc[:,0]  #col as series
mt.iloc[:,0:2]  #col as series

#select cols
mt['mpg'] #series
mt[['mpg']]  #DF
mt[['mpg','wt']]  #list of cols
mt[mt['mpg']]  #col as series
#select rows
mt[['mpg','wt']]
mt2 = mt.reset_index()# index as integers
mt2[['mpg','wt']]
mt2[1:5]
mt2[mt2['mpg'] > 25, 'mpg']
mt2.loc[3:5]
mt2.iloc[0]

#select/filter
mt.filter(items=['mpg','am'])
mt2.filter(items=[5], axis=0)
mt2.filter(like='m')
mt.filter(like='Ma', axis=0)
mt.filter(regex='p')


#%%% indexing
len(mt)
range(len(mt))
mt.reindex(index=range(len(mt)))
mt2
mt2.index.has_duplicates
mt2.index.is_monotonic_increasing
mt2.index.nlevels
mt.index.nlevels

mt2.index.nunique
mt2.index.min()
mt2.index.max()
mt.index.min()
mt.index.max()
#group by index
mt.groupby(level=0).size()
#create index col as gear
mt2B = mt.set_index('gear')
mt2B.groupby(level=0).size()

#%%% SUMMARIES
mt.dtypes
mt.cyl.value_counts()
mt['cyl'].value_counts()
mt['cyl'].value_counts().reset_index()
mt['cyl'].value_counts().reset_index(name='count')
mt.groupby('cyl').size() #.group.reset_index(name='count')
mt.groupby('cyl').size().reset_index(name='count')

mt.groupby(['am','cyl','gear']).size()
mt.groupby(['am','cyl'])['gear'].count()
mt.groupby(['am','cyl'])['gear'].agg('count')
#resetindex
mt.groupby(['am','cyl'])['gear'].agg('count').reset_index() #flat table
mt.groupby(['am','cyl'], as_index=False)['gear'].agg('count') #flat table

mt.groupby('cyl').value_counts()

#multiple summaries
mt.groupby(['am','gear'])['mpg'].agg('mean')
mt.groupby(['am','gear'], as_index=False)['mpg'].agg('mean').fillna('100')
mt.groupby(['am','gear'], as_index=False)['mpg'].agg(['count','mean'])
mt.groupby(['am','gear'], as_index=False)['mpg'].agg(['count','mean']).reset_index()

#not best way
mt.groupby(['am','gear'], as_index=False)['hp', 'mpg'].agg(['count','mean'] ).reset_index()
mt.groupby(['am','gear']).agg({'hp':['count','mean'], 'mpg':['min', 'max']}).reset_index()
mt.groupby(['am','gear'], as_index=False).agg({'hp':['count','mean'], 'mpg':['min', 'max']})
#https://github.com/DUanalytics/pyAnalytics/blob/master/91-CaseStudy/case_grouping.py
#%%%Missing Data
mtS1A = mt.groupby(['gear','am']).size().reset_index(name='count')
mtS1A
mtS1B = mt.groupby(['gear','am'])['mpg'].agg(np.mean).reset_index()
mtS1B
mtS1C = mt.groupby(['gear','am']).agg({'mpg':np.mean, 'wt':[np.min, np.max]}).reset_index()
mtS1C #2 levels of index
mtS1C.columns.levels
mtS1C.columns.droplevel()
mtS1C.droplevel(0, axis='columns')
mtS1C.columns.get_level_values(1)
mtS1C.columns.get_level_values(0)

mtS1C.xs
mtS1C2 = mtS1C.droplevel(0, axis='columns')
mtS1C2
mtS1C2.columns = ['gear','am','meanMPG','minWt','maxWt']
mtS1C2

#%%%Pandas Plots
#plot-kind
mt.groupby('gear').size()
mt.groupby('gear').size().plot(kind='bar')
mt.groupby('carb').size().plot(kind='barh')
mt.mpg.plot(kind='hist')
mt.hp.plot(kind='box')
mt.hp.plot(kind='kde')
mt.hp.plot(kind='density')
mt.plot.scatter(x='wt', y='mpg', c='hp', colormap='winter_r') #DF
mt.groupby('cyl').size().plot(kind='pie')
mt.groupby('cyl').size().plot(kind='pie')

#grouping-rename-wide-long
mt.groupby(['gear','am']).agg({'mpg':np.mean}).reset_index()
mt.groupby(['gear','am']).agg({'mpg':np.mean}).reset_index().set_index(keys='gear')
mtS2A= mt.groupby(['gear','am']).agg({'mpg':np.mean} ).reset_index().pivot_table( index='gear', columns='am', values='mpg', fill_value=0).add_prefix('am')
mtS2A
mtS2B= mt.groupby(['gear','am']).agg({'mpg':np.mean} ).reset_index().pivot_table( index='gear', columns='am', values='mpg', fill_value=0).add_prefix('am').reset_index()
mtS2B

#DF---
mt[['hp','mpg']].plot.scatter(x='mpg', y='hp',c='b') #DF
mt.plot.scatter(x='mpg', y='hp', c='gear', colormap='viridis') #DF
mt.sort_values(by='wt').plot.line(x='wt', y='mpg',c='g')  #line better with TS
mtS2A.plot.area(y='am1')  #x will be index
mtS2B.plot.area(x='gear', y='am1')  #x will be index gear col
#mtS2A has index, mtS2B does not have
mtS2A.plot.area(stacked=True, title='Area Pandas Plot- Stacked')
mtS2A.plot.area(stacked=False, table=True, title='Area Pandas Plot')




#subplots------
mt.sort_values(by='wt').plot.line(x='wt', y='mpg', subplots=False)
mtS2B.plot.area(x='gear', stacked=False, subplots=True)
mtS2A.plot.line(subplots=True, legend=True)



#%%% Matplotlib Plots

plt.plot((1,2,3,4))
plt.ylabel('Some Numbers')
plt.show();
#--------
plt.plot([1,2,3,4],[4,8,3,5], 'ro')
plt.axis([0,5,0,10])   #axis dim : x, y
plt.ylabel('Some x & y Numbers')
plt.show();
#-----------
t = np.arange(start=10, stop=100, step=5)
t
plt.plot(t, t, 'r--')
plt.show();

plt.plot(t, t, 'r--',   t, t**2, 'bs',  t, t**3/100, 'g^')
plt.show(); # x1,y1; x2,y2; x3,y3

plt.plot(t, linestyle='dotted', color='r', linewidth=5)
plt.plot(t*2, linestyle='dashed', color='hotpink', linewidth='20')
plt.plot(t*3, ls=':', c='#4CAF50', linewidth='10')
plt.show();
#linestyles = -, :, --, -., ", ''
#%%%bars
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x,y)
plt.show();

plt.barh(x, y)
plt.show();

plt.bar(x, y, color = "red", width=.7)
plt.show();

plt.barh(x, y, color = "blue", height=.5)
plt.show();
#%%% Histogram
x = np.random.normal(170, 10, 250)
x

plt.hist(x)
plt.show();


#%%% Pie
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y)
plt.show() ;

plt.pie(y, labels = mylabels)
plt.show() ;

plt.pie(y, labels = mylabels, startangle = 180)
plt.show() ;# 1st wedge at 180, dates-Apples

myexplode = [0.5, 0, 0, 0]
mycolors = ["black", "hotpink", "b", "#4CAF50"]
plt.pie(y, labels = mylabels, explode = myexplode, shadow=True, colors=mycolors)
plt.legend()
plt.legend(title = "Four Fruits:")
plt.show() ;#wedge 0.5 from the center of the pie
#colors - r, g, b, c, m, y, k, w
#%%% Seaborn
sns.pairplot(mt)


#%%% pending topics
#drop col
#merge DF
#join DF
#concat DF
#search for values
#regex
#create dict from DF
#import from different sources
#set datatypes when importing
#duplicates
#missing values
#is in 
#pivot table
#crosstab
#reshape/melt
#stack/unstack
#datetime manipulation
