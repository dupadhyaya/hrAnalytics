# -*- coding: utf-8 -*-
#Created by DU 
#Topic : Employee Attritution & Performance
#%%%libraries
import pandas as pd # Data Processing
import numpy as np  #numerical Python
import matplotlib.pyplot as plt  #Graphs
import seaborn as sns # Advance Graphs
import warnings # warning messages
import datetime as dt
import pydataset as data
import os #OS functionality
#%%%
#We will try to analyse visually the trends in how and why are quitting their jobs. Is it because of monthly income level, or distance from home or performance ratings? As an initial step, we evaluate data using visual analytics. We will use seaborn (majorly) and matplot library
warnings.filterwarnings("ignore") #Never print the matching warning
#%%%Read Data
folderFile = '../data/set3/WA_Fn-UseC_-HR-Employee-Attrition.csv'
linkedFile = 'https://raw.githubusercontent.com/dupadhyaya/hrAnalytics/main/data/set3/WA_Fn-UseC_-HR-Employee-Attrition.csv'
hr1 = pd.read_csv(folderFile, header=0)
hr2 = pd.read_csv(linkedFile, header=0)
hr1.shape #folder
hr2.shape #link
hr = hr2.copy()
hr.shape
#%%%#Read the dataset
hr.head() #Display first 5 rows of the data
hr.columns
pd.set_option('display.max_rows', 20)
pd.set_option('display.max_columns', 6)
pd.set_option('display.width', 1000)
hr.columns
hr.head()
#%%% Study and understand the values 
hr.dtypes
hr.shape  #1470 rows x 35 columns
hr.describe(include='all')
#%%% Simple plot
sns.distplot(hr['Age'])
plt.show()
hr.columns
selCols1 = ['Age', 'TotalWorkingYears', 'YearsAtCompany', 'YearsInCurrentRole']
hr[selCols1].head()
#%%%#show multiple plots together
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(10,10))
plt.suptitle('Distribution of various Factors', fontsize=20)
sns.distplot(hr[selCols1[0]], ax=ax[0,0] )
ax[0][0].set_title('Distribution of Age')
sns.distplot(hr[selCols1[1]], ax=ax[0,1] )
ax[0][1].set_title('Distribution of Work Exp')
sns.distplot(hr[selCols1[2]], ax=ax[1,0] )
ax[1][0].set_title('Distribution of Service in Coy')
sns.distplot(hr[selCols1[3]], ax=ax[1,1] )
ax[1][1].set_title('Distribution of Years in Current Role')
plt.show();
#%%% Count Plot
#%matplotlib inline
hr.columns
hr.dtypes
hr.Attrition.value_counts()
sns.countplot(data=hr, x='Attrition')
plt.show();
#250 persons left during the period
#what was the monthly income of Yes persons
sns.barplot(data=hr, x='Attrition', y='MonthlyIncome', hue='Gender', estimator='median')
plt.show();
#%%%
#what was the monthly income of Yes persons
sns.barplot(data=hr, x='Attrition', y='MonthlyIncome', hue='JobSatisfaction', estimator='median')
plt.show();

#%%%Violin Plot
sns.violinplot(x="Attrition", y="YearsAtCompany", hue="Gender", data=hr, palette="muted", split=True,  inner="stick")
plt.show();
#violin plots are similar to box plots but they have the capability to explain the data better. The distribution of data is measured by the width of the violin plot. Here, we have plotted the number of years spent in an organization based on gender. The middle dashed line shows the median. The lines above and below the median show the interquartile range. The denser part shows the maximum population falls under that range and thinner part shows the lesser population. 
#%%%Joint Plot (Scatter + Histogram)
sns.jointplot(data=hr, x='Age', y='MonthlyIncome', kind = "scatter")   
plt.show();
#Scatter plot shows the relationship between Age and Monthly Income. We can find a linear relationship. Further, the density plot above shows the distribution of age while density plot in the right shows the distribution of the monthly income.
#%%%Factor Plot and Facet Grid
hr['age_group'] = pd.cut(hr['Age'], 3, labels=['Young', 'Middle', 'Senior'])
hr['age_group'].describe()
hr['age_group'].value_counts()

#Slicing the continuous data into various groups 
#Age Group is the name of new column

sns.catplot(   x =   'Attrition',     # Categorical
               y =   'MonthlyIncome',      # Continuous
               hue = 'JobLevel',    # Categorical
               col = 'age_group',   # Categorical
               col_wrap=2,           # Wrap facet after two axes
               kind = 'box',
               data = hr)
plt.show();
# monthly income plays an important role in retaining the employees in an organization. It can be observed across job levels and different age groups.
#%%%Facet Plot
g = sns.FacetGrid(hr, col="JobSatisfaction", row="Gender")
g.map(sns.kdeplot, "MonthlyIncome", "YearsInCurrentRole")
plt.show();
#kernel density estimation plot. It displays the density distribution of two continuous variables (namely, Monthly income and years in current role). We have created facets according to different job satisfaction levels and gender.
#%%%Pair Plot
selCols2 = ['Attrition','Age','MonthlyIncome','DistanceFromHome']
sns.pairplot(hr[selCols2], kind="reg", diag_kind = "kde" , hue = 'Attrition' )
plt.show();
#Pairwise plots between continuous variables show the relationship between them. For example. observing the relationship between Age and Monthly Income, we can find that with age, monthly income has increased but the increase is not similar for both groups (Attrition and Retention).
#%%%Pair Plot-2
selCols3 = ['Gender', 'HourlyRate','DailyRate','MonthlyRate','PercentSalaryHike']
sns.pairplot(hr[selCols3], kind="reg", diag_kind = "kde" , hue = 'Gender' )
plt.show();
#The above plot does not convey much of any relationship between variables across gender. This shows that hourly rate, daily rate, monthly rate and percent salary hike is same for both female and male employees.

#%%%Heat Plot
#Plot a correlation map for all numeric variables
f,ax = plt.subplots(figsize=(18, 18))
sns.heatmap(hr.corr(), annot=True, linewidths=.4, fmt= '.1f',ax=ax, annot_kws={'fontsize':20})
plt.show();
#Two variables are said to be highly correlation when they have a value of 0.7 or greater. The correlation plot between all continuous variables indicate that years at company and year with current manager, years in current role and years with current manager, monthly income and total working years, age and total working years, percent salary hike and performance rating are highly correlated
sns.set(font_scale=1.5)
f,ax = plt.subplots(figsize=(18, 18))
sns.heatmap(hr[selCols1].corr(), annot=True, linewidths=.4, fmt= '.1f',ax=ax, vmin=.5, vmax=.9, linecolor='w', linewidth=1, cbar=False, annot_kws={'fontsize':12}) #vminmax - color scale
plt.show();

#--------
f,ax = plt.subplots(figsize=(18, 18))
sns.heatmap(hr.corr(), annot=True, linewidths=.4, fmt= '.1f',ax=ax, vmin=.5, vmax=.9, cbar=False)
plt.show();

#%%%Violin Plot
#%%%Violin Plot

#%%%Links
#https://www.kaggle.com/code/kukreti12/hr-analytics-using-python
