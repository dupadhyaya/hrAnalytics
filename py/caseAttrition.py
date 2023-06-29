# -*- coding: utf-8 -*-
#Created by DU 
#Topic : Employee Attrition
#%%%
#libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
from pydataset import data
import os
import glob
#%%%
os.listdir('./data/')
root_dir='./data/'
for filename in glob.iglob(root_dir + '**/**', recursive=True):
     print(filename)
dataFile ='./data/misc/HR_employeeAttrition.csv'     
#%%%
df = pd.read_csv(dataFile)
df.shape
df.columns
df.head().filter(items=['Age', 'Attrition','Department'])
#%%%
df.describe()
df.dtypes
#catCols
df.select_dtypes(include=object).columns.tolist()

cat_cols=df.select_dtypes(include=object).columns.tolist()
cat_cols
#numeric
df.select_dtypes(include='int64').columns.tolist()

#%%%
cat_df=pd.DataFrame(df[cat_cols].melt(var_name='column', value_name='value')                  .value_counts()).rename(columns={0: 'count'}).sort_values(by=['column', 'count'])
cat_df.head()
display(df.select_dtypes(include=object).describe())
display(cat_df)
cat_df.columns
#%%%EDA

fig, ax = plt.figure()
ax= sns.countplot(df, x='Attrition', hue='Gender', order = df.Attrition.value_counts(ascending=False).index)
abs_values = df['Attrition'].value_counts(ascending=False).values
ax.bar_label(container=ax.containers[0], labels=abs_values)
plt.show();

#%%%
ax= sns.countplot(df, x='Attrition', hue='Gender')
abs_values = df['Attrition'].value_counts(ascending=False).values
for label in ax.containers:
    ax.bar_label(label)
plt.show();

ax= sns.countplot(df, x='Attrition', hue='Department')
abs_values = df['Attrition'].value_counts(ascending=False).values
for label in ax.containers:
    ax.bar_label(label)
plt.show();

df1B = df[df['Attrition']== 'Yes'].filter(items= ['Department','Attrition','Gender'])
df1B
pieValues=df1B['Department'].value_counts(dropna=True)
pieLabels = df1B['Department'].dropna().unique()
ax = plt.pie(x=pieValues,  autopct= lambda x: '{:.0f}'.format(x*pieValues.sum()/100), startangle=0)
plt.legend(pieLabels)
plt.show();

pieValues=df1B['Gender'].value_counts(dropna=True)
pieLabels = df1B['Gender'].dropna().unique()
ax = plt.pie(x=pieValues,  autopct= lambda x: '{:.0f}'.format(x*pieValues.sum()/100), startangle=0)
plt.legend(pieLabels)
plt.show();

#%%%%
df1C = df.groupby(['Gender','Department'])['Attrition'].value_counts(normalize=True).mul(100).rename('percent').reset_index().round(0)
df1C.head()

plt.figure(figsize=(8,6))
g = sns.FacetGrid(data=df1C, col='Department', row='Gender', hue='Attrition')
g.map(plt.bar, 'Attrition','percent').add_legend()
plt.show();
#%%%
df['WorkLifeBalance'].value_counts()
df1D = df.groupby(['Gender','WorkLifeBalance'])['Attrition'].value_counts(normalize=True).mul(100).rename('percent').reset_index().round(0)
df1D.head()

plt.figure(figsize=(8,6))
g = sns.FacetGrid(data=df1D, col='WorkLifeBalance', row='Gender', hue='Attrition')
g.map(plt.bar, 'Attrition','percent').add_legend()
plt.show();

#%%% avg salaries by Job role
cols1 = ['MonthlyIncome','JobRole']
sorted(df.columns.values)
df[cols1]

salJobSum1 = df[cols1].groupby('JobRole')['MonthlyIncome'].agg(np.mean).reset_index().round().sort_values(by='MonthlyIncome')
salJobSum1

plt.bar(x=salJobSum1.JobRole, height=salJobSum1.MonthlyIncome)
plt.show();

salJobSum1.boxplot(column = 'MonthlyIncome') #, by = 'JobRole' )
salJobSum1.boxplot(column = 'MonthlyIncome', by = 'JobRole' )
plt.boxplot(x= salJobSum1.MonthlyIncome)
#%%% 
!pip install researchpy

#%%%Links
#https://www.kaggle.com/code/kellibelcher/hr-analytics-and-prediction-of-employee-attrition/notebook

