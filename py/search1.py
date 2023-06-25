# -*- coding: utf-8 -*-
#Created by DU 
#Topic : Search Replace Regex Filter
#%%%
#libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
from  pydataset import data
#%%%
mt = data('mtcars')
mt['carnames'] = mt.index
mt=mt.reset_index()
mt.head()
#%%% Search

mt['mpg']
mt['mpg'] > 25
mt[mt['mpg'] > 25]
mt[(mt['mpg'] > 25) & (mt['mpg'] < 30)]
mt.query('mpg > 25')
mt.loc[mt['mpg'] > 25, ['carnames','wt','mpg']]
mt[['mpg','carnames']].where(mt['mpg']> 25)

#%%% String search
mt['carnames']
mt[['carnames','mpg']]
mt['carnames'].str.find('Mazda')  #series
mt.carnames.str.find('Mazda')
mt.carnames.str.contains('Mazda')
mt.carnames[mt.carnames.str.contains('Mazda')]  #2
mt[mt.carnames.str.contains('Mazda')]  #2
mt.loc[mt.carnames.str.contains('Mazda'),['carnames','mpg']]  #2
mt.loc[mt.carnames.str.contains('Mazda', case=False),['carnames', 'mpg']]
#starts with
mt[mt.carnames.str.startswith('M')].filter(items=['carnames','mpg'])
#%%% regex
#seq of char that specifies a match pattern in text.... 
# re can contain special(|,(. )and ord char (a, A, 0).. 
#https://docs.python.org/3/library/re.html
#https://kanoki.org/2019/11/12/how-to-use-regex-in-pandas/

#%%%

#regex=True by default
mt.carnames
mt.carnames.str.count(r'(^M.*)')  #1 values
mt.carnames.str.count(r'(^M.*)').sum()
mt.carnames[mt.carnames.str.count(r'(^M.*)')==1]
#findall
[item[0] for item in mt.carnames.str.findall('^[MP].*') if len(item) > 0]
#contains
mt[mt.carnames.str.contains('^M.*', regex=True)].filter(items=['carnames','mpg'])
mt.loc[mt.carnames.str.contains('^M.*'), ['carnames','mpg']]
mt.loc[mt.carnames.str.contains('280'), ['carnames','mpg']]
mt.query('carnames.str.contains("^M").values').filter(items=['carnames','mpg'])
#match
re1='Merc 230'
mt[mt.carnames.str.match(re1)].filter(items=['carnames','mpg'])
re2='Merc.*'
mt[mt.carnames.str.match(re2)].filter(items=['carnames','mpg'])
re3='M.*'  #starts with M
mt[mt.carnames.str.match(re3)].filter(items=['carnames','mpg'])

#starts with


#extract
re5='([A-Z]a)'  #any capital letter followed by a
mt.carnames.str.extract(pat=re5)
re6="" #first 8 char
mt.carnames.str[0:8]
#%%% find / replace
#1 with 100
mt.replace(1,100).filter(items=['carnames','mpg','am','vs'])
mt.replace(to_replace=[0,1], value=100).filter(items=['carnames','mpg','am','vs'])
#mazda with jazz
mt.replace(to_replace='Mazda RX4', value='Jazz').filter(items=['carnames','mpg','am','vs'])
mt.replace(to_replace='Merc', value='Jazz', regex=True).filter(items=['carnames','mpg','am','vs'])
#https://pandas.pydata.org/docs/reference/api/pandas.Series.str.replace.html
mt.carnames.str.replace('Mazda', 'Jazz')  #part of the string
mt.carnames.str.replace(pat='merc', repl='Jazz', case=False, regex=True)  #part of the string


#%%%https://docs.python.org/3/library/re.html

import re
re.search(string ='Dhiraj Upadhyaya' , pattern = 'aj')
re.match(string ='Dhiraj Upadhyaya' , pattern = 'aj')
re.split(pattern ='Dhiraj Upadhyaya', string='j')
