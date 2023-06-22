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
import requests
from bs4 import BeautifulSoup
#%%%
# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/List_of_cities_in_India_by_population"
table_class="wikitable sortable jquery-tablesorter"
response=requests.get(wikiurl)
print(response.status_code)
#%%%
# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find('table',{'class':"wikitable sortable"})
indiatable
#%%%
df1=pd.read_html(str(indiatable))
df1
df1[0]
# convert list to dataframe
df=pd.DataFrame(df1[0])

print(df.head())
df.columns
type(df)
df.shape
df.columns = ['rank2011', 'city','pop2011', 'pop2001', 'stateUT']
df
#%%% 
df.head()
df.pivot(columns='stateUT')
#%%%

#%%%

#%%%Links
#https://medium.com/analytics-vidhya/web-scraping-a-wikipedia-table-into-a-dataframe-c52617e1f451

