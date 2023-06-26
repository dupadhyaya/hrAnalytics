# -*- coding: utf-8 -*-
#Created by DU 
#Topic : Start Plotting in MPL
#pip install ipympl
#%%%
#libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
from pydataset import data
#%%%
mt = data('mtcars')
mt.sort_values(by='wt', inplace=True)
mt.columns
numCols = ['wt','mpg','hp','disp', 'qsec']
mt[numCols]
%matplotlib inline
plt.close('all')
plt.cla()
plt.clf()
%clear
#%reset
#%%% plot1
%matplotlib   #ipyconsole
plt.plot(mt.wt, mt.mpg)
plt.show();

%matplotlib inline  
plt.plot(mt.wt, mt.mpg)
plt.show();
#single plot
fig, ax = plt.subplots() 
ax.plot(mt.wt, mt.mpg)
ax.set_title('Wt vs Mpg')
plt.show();
#rows-2 with index ax[0]....
fig, ax = plt.subplots(nrows=2) 
ax[0].plot(mt.wt, mt.mpg)
ax[0].set_title('Wt vs Mpg')
ax[1].plot(mt.wt, mt.hp)
ax[1].set_title('Wt vs HP')
fig.suptitle(' Wt vs (MPG & HP) -G1')
plt.show();
#rows-2  with ax1...
fig, (ax1, ax2) = plt.subplots(nrows=2) 
ax1.plot(mt.wt, mt.mpg)
ax1.set_title('Wt vs Mpg')
ax2.plot(mt.wt, mt.hp)
ax2.set_title('Wt vs HP')
fig.suptitle(' Wt vs (MPG & HP) -G2')
plt.show();

#rows and cols, with sharedX axis
fig, ax = plt.subplots(nrows=2, ncols=2, sharex=True) 
ax[0,0].plot(mt.wt, mt.mpg)
ax[0,0].set_title('Wt vs Mpg - 0,0')
ax[1,0].plot(mt.wt, mt.hp)
ax[1,0].set_title('Wt vs HP - 1,0')
ax[0,1].plot(mt.wt, mt.qsec)
ax[0,1].set_title('Wt vs qsec - 0,1')
ax[1,1].plot(mt.wt, mt.disp)
ax[1,1].set_title('Wt vs disp - 1,1')
fig.suptitle(' Wt vs (MPG ,HP, QSEC, DISP) -G3 with shared X axis')
plt.show();

#using ravel Flatten
len(numCols)
numCols1 = numCols[1:5]
numCols1
for i in range(len(numCols1)):    print(i, numCols1[i])
fig, axs = plt.subplots(nrows=2, ncols=2, sharex=True, figsize=(15,6), edgecolor='r') 
axs.shape  #(2,2)
axs = axs.ravel()
axs
axs.shape
fig.subplots_adjust(hspace=1, wspace=.01)
axs[0].plot(mt['wt'], mt[numCols1[0]]) 
axs[1].plot(mt['wt'], mt[numCols1[1]]) 
axs[2].plot(mt['wt'], mt[numCols1[2]]) 
axs[3].plot(mt['wt'], mt[numCols1[3]]) 
fig.suptitle('Multipe Plots using Loop')
fig.supxlabel('Weight')
plt.show();

 
#https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html
#%%% seaborn
import seaborn as sns
sns.barplot(data=mt, x='am', y='mpg', estimator='mean')
sns.barplot(data=mt, x='am', y='mpg', estimator='max')
sns.countplot(data=mt, x='am')
sns.countplot(data=mt, x='am', hue='gear')
#%%%https://seaborn.pydata.org/generated/seaborn.barplot.html
pn = sns.load_dataset('penguins')
pn.head()
pn.columns
pn.filter(items=['island','body_mass_g']).head()
sns.barplot(data=pn, x='island', y='body_mass_g')

#%%%
%matplotlib
fig, axs = plt.subplots(nrows=2, ncols=2) 
sns.countplot(ax=axs[0,0], data=mt, x='am')
sns.countplot(ax=axs[0,1], data=mt, x='am', hue='vs')
sns.countplot(ax=axs[1,0], data=mt, x='am', hue='gear')
sns.countplot(ax=axs[1,1], data=mt, x='am', hue='carb')
plt.show();
#%%%

#%%%

#%%%
