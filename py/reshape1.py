# -*- coding: utf-8 -*-
#Created by DU 
#Topic : ---------
#%%%
#libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import pydataset as data
import random
from itertools import product

#%%%
n1=4*2
dept = ['HR','Marketing', 'Finance', 'Operations']
coy =['TCS','HCL']
coyID1 = ['coyA' + str(i) for i in range(1,4+1)]
coyID1
coyID2 = ['coyB' + str(i) for i in range(1,4+1)]
coyIDs = coyID1 + coyID2
coyIDs

hrSum1A = pd.DataFrame(list(product(dept, coy)), columns=['dept', 'coy'])
hrSum1A['coyID'] = coyIDs
hrSum1A

#add values

M = np.random.randint(low=5, high=10, size=n1)

M
F = np.random.randint(low=3, high=7, size=n1)
for i in [hrSum1A,M,F]: print(len(i))

hrSum1B = pd.DataFrame({'coyID':coyIDs, 'M':M, 'F':F})
hrSum1B
#2 Df with common cols

#%%%merge

hrSum2 = pd.merge(hrSum1A, hrSum1B)
hrSum2

#%%% melt  : wide to long
hrSum2melt = pd.melt(frame=hrSum2, id_vars=['coyID','coy','dept'], value_vars=['M','F'], var_name='gender', value_name='count') 
hrSum2melt
#%%% pivot
hrSum2melt.pivot(index=['coyID','coy','dept'], columns=['gender'], values = 'count').reset_index().rename(columns={'gender':'ID'})

hrSum2pivot = hrSum2melt.pivot(index=['coyID','coy','dept'], columns=['gender'], values = 'count').reset_index().rename_axis(None, axis=1)
#same as above
#%%% crosstab https://pandas.pydata.org/docs/reference/api/pandas.crosstab.html
genders = ['M','F']
pd.crosstab(coy, genders)
CT1 = hrSum2melt.groupby(['coy','dept'])['count'].agg(np.sum).reset_index()
CT1
CT1.dtypes
pd.crosstab(columns= CT1.coy, index=CT1.dept, values=CT1.count, aggfunc='mean')
#%%% pivot_table
hrSum2PT1 = pd.pivot_table(CT1, values='count', index='dept', columns='coy').reset_index().rename_axis(None, axis=1)

#%%%  wide to long  with stub names
#A2022, B2021
hrSum2
pd.wide_to_long(hrSum2, stubnames =['M','F'],  i='coyID')
#%%%  stack


#%%% unstack

#%%%  links
#https://towardsdatascience.com/wide-to-long-data-how-and-when-to-use-pandas-melt-stack-and-wide-to-long-7c1e0f462a98#:~:text=melt()%2C%20.,Wide%20to%20a%20Long%20format.

