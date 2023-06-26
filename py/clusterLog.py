# -*- coding: utf-8 -*-
#Created by DU 
#Topic : Clustering - Grouping employees
#%%%
#libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
from pydataset import data
import os
%matplotlib --list
%matplotlib inline
#inline automatic
#%%% Techniques
#Clustering
#Attritution
#%%% Clustering Libraries
from sklearn.cluster import KMeans


#%%%Import Data
folder ='../data/misc/' 
link1 =''
os.listdir(folder)
hrData1 = pd.read_csv('../data/misc/HR_comma_sep.csv')
hrData1.head()
hrData1.columns
hrData1.shape
hrData1.columns =['satLevel','lastEval', 'nProjects','avgMonHrs','tenureCoy', 'workAccd', 'left', 'promL5Y', 'dept', 'salary']
hrData1.head()
hrData1.describe()
catCols = ['workAccd','left','promL5Y', 'dept','salary']
numCols = ['satLevel','lastEval','nProjects','avgMonHrs']
hrData1[catCols] = hrData1[catCols].astype('category') 
hrData1.dtypes
#%%% Problem Objectives-----
#1- Do Exploratory Data analysis to figure out which variables have a direct and clear impact on employee retention (i.e. whether they leave the company or continue to work)
#2- Plot bar charts showing the impact of employee salaries on retention
#3- Plot bar charts showing a correlation between department and employee retention
#4- Now build a logistic regression model using variables that were narrowed down in step 1
#5- Measure the accuracy of the model
#%%% Describe Data
#duplicates 
sum(hrData1.duplicated()) #3008 duplicates
hrData1.isna().sum()   # no missing values
hrData2A = hrData1.drop_duplicates()
sum(hrData2A.duplicated())
hrData2A.columns
#%%%% Summarise Data
#%%% Visualise Data
hrData2A[numCols].head()
hrData2A.boxplot(column=numCols)
hrData2A.tenureCoy.plot(kind='hist')

#%%%Model Data

#%%%Evaluate

#%%%Conclude

#%%%% Links
#https://www.kaggle.com/code/yingsunwan/employee-retention-prediction
