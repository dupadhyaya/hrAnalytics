# -*- coding: utf-8 -*-
#Created by DU 
#Topic : Reshpaing Data
#%%%#libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
from pydataset import data
import random
from itertools import product
#%%%
n1=4*2
dept = ['HR','Marketing', 'Finance', 'Operations']
coy =['TCS','HCL']
ID1 = ['coyA' + str(i) for i in range(1,4+1)]
ID1
ID2 = ['coyB' + str(i) for i in range(1,4+1)]
IDs = coyID1 + coyID2
IDs

hrSum1A = pd.DataFrame(list(product(dept, coy)), columns=['dept', 'coy'])
hrSum1A['ID'] = IDs
hrSum1A

#add values
M = np.random.randint(low=5, high=10, size=n1)
M
F = np.random.randint(low=3, high=7, size=n1)
for i in [hrSum1A,M,F]: print(len(i))

hrSum1B = pd.DataFrame({'ID':IDs, 'M':M, 'F':F})
hrSum1B
#2 Df with common cols

#%%%merge
hrSum2 = pd.merge(hrSum1A, hrSum1B)
hrSum2

#%%% melt  : wide to long
hrSum2melt = pd.melt(frame=hrSum2, id_vars=['ID','coy','dept'], value_vars=['M','F'], var_name='gender', value_name='count') 
hrSum2melt

#%%% pivot
hrSum2melt.pivot(index=['ID','coy','dept'], columns=['gender'], values = 'count')
hrSum2melt.pivot(index=['ID','coy','dept'], columns=['gender'], values = 'count' ).reset_index().rename(columns={'gender':'ID'})

hrSum2pivot = hrSum2melt.pivot(index=['ID','coy','dept'], columns=['gender'], values = 'count').reset_index().rename_axis(None, axis=1)
hrSum2pivot
#same as above
#%%% crosstab https://pandas.pydata.org/docs/reference/api/pandas.crosstab.html
genders = ['M','F']
pd.crosstab(coy, genders)
CT1 = hrSum2melt.groupby(['coy','dept'])['count'].agg(np.sum).reset_index()
CT1
CT1.dtypes
pd.crosstab(columns= CT1.coy, index=CT1.dept, values=CT1.count, aggfunc='mean')
#%%% pivot_table
pd.pivot_table(CT1, values='count', index='dept', columns='coy')
hrSum2PT1 = pd.pivot_table(CT1, values='count', index='dept', columns='coy').reset_index().rename_axis(None, axis=1)
hrSum2PT1
#%%%  wide to long  with stub names
#wide cols start with janxx
car = ['Jazz', 'Innova','Kia','BMW']
fuel = ['Petrol','Diesel','Petrol','Diesel']
jan23 = np.random.randint(5,10,4)
jan22 = np.random.randint(6,11,4)
jan21 = np.random.randint(5,13,4)
carMPG = pd.DataFrame({'car':car, 'fuel':fuel, 'jan23':jan23, 'jan22':jan22, 'jan21':jan21})
carMPG
pd.wide_to_long(carMPG, stubnames='jan', i=['car'], j='year')
pd.wide_to_long(carMPG, stubnames='jan', i=['car'], j='year').rename(columns={'jan':'mpg'}).reset_index()

#%%%  stack
#discuss later
carsMPG2 = pd.DataFrame({'car':car, 'fuel':fuel, 'jan23':jan23, 'jan22':jan22})
carsMPG2
carsMPG2.stack()
carsMPG2.stack(1)  #error

mpgJan = pd.MultiIndex.from_tuples([('mileage','jan23'), ('mileage','jan22')])
mpgJan
#discuss later

#%%% unstack
carsMPG2.unstack(level=0)
#%%%  links
#https://towardsdatascience.com/wide-to-long-data-how-and-when-to-use-pandas-melt-stack-and-wide-to-long-7c1e0f462a98#:~:text=melt()%2C%20.,Wide%20to%20a%20Long%20format.

