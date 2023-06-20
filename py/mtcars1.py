# -*- coding: utf-8 -*-
#Created by DU 
#Topic : General Practise on Pandas and Matplotlib
#%%%
#libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import style
import seaborn as sns
import datetime as dt
from pydataset import data
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
catCols = ['am','vs','gear','cyl','carb']
numCols = ['mpg','disp', 'hp', 'drat', 'qsec']
catCols
numCols
mt[numCols]
mt[catCols] = mt[catCols].astype('category')
mt[catCols]
mt.describe(include='all')
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
sns.pairplot(mt)
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
#%%%
mt.to_dict()
mt.to_clipboard()
mt.to_excel()
mt.to_csv()
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



#%%%Plots

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
#%%% Histogram