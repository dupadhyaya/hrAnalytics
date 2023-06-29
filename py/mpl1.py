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
%matplotlib
plt.plot(mt.wt, mt.mpg)
plt.show();

%matplotlib inline  
plt.plot(mt.wt, mt.mpg)
plt.show();

#single plot
fig, ax = plt.subplots() 
ax.plot(mt.wt, mt.mpg, label='wt vs mpg')
#ax.minorticks_on()
ax.grid(which='major', color='red')
ax.set_title('Wt vs Mpg')
ax.legend()
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
ax1.plot(mt.wt, mt.mpg, label = 'Wt-MPG')
ax1.set_title('Wt vs Mpg')
ax2.plot(mt.wt, mt.hp, label='Wt-HP')
plt.xlabel('Wt')
ax2.set_title('Wt vs HP')
fig.suptitle(' Wt vs (MPG & HP) -G2')
plt.legend()
plt.show();

#rows and cols, with sharedX axis
fig, ax = plt.subplots(nrows=2, ncols=2, sharex=True) 
ax[0,0].plot(mt.wt, mt.mpg, label='G1')
ax[0,0].set_title('Wt vs Mpg - 0,0')
ax[1,0].plot(mt.wt, mt.hp,  label='G1')
ax[1,0].set_title('Wt vs HP - 1,0')

ax[0,1].plot(mt.wt, mt.qsec,  label='G233')
ax[0,1].set_title('Wt vs qsec - 0,1')
ax[0,1].legend('upper left')
ax[1,1].plot(mt.wt, mt.disp , label='G1')
ax[1,1].set_title('Wt vs disp - 1,1')
ax[1,1].set_xlim((1,40))

fig.suptitle(' Wt vs (MPG ,HP, QSEC, DISP) -G3 with shared X axis')
plt.legend()
plt.draw()
plt.show();
plt.close('all')
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
plt.show?
 
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
#%%% Violin plot
fig, ax = plt.subplots()
data = np.random.normal(0, 6, 100)
ax.violinplot(data, showmeans=False, showmedians=True)
plt.show();

fig, ax = plt.subplots()
data = mt[['mpg','wt','hp']]
ax.violinplot(data, showmeans=True, showmedians=True)
plt.show();

#%%%
fig, ax = plt.subplots()
ax.scatter(x=mt.wt, y=mt.mpg, s=mt.gear, c=mt.am, alpha=0.6,label='wt vs mpg')
ax.set_title('Scatter plot of x-y pairs semi-focused in two regions')
ax.set_xlabel('x value')
ax.set_ylabel('y value')
plt.legend()

plt.show()
#%%%
%matplotlib inline
x = np.arange(-5, 5, 0.01)
y = x**2
fig, ax = plt.subplots()
# Plot a line
ax.plot(x, y)

# first annotation relative to the data
ax.annotate('function minium \n relative to data', xy=(0, 0),   xycoords='data',  xytext=(1, 1), arrowprops=  dict(facecolor='black', shrink=0.05), horizontalalignment ='left',  verticalalignment ='top')


# second annotation relative to the axis limits
bbox_props = dict(boxstyle="round,pad=0.5", fc="w", ec="k", lw=2)


ax.annotate('half of range \n relative to axis limits',
            xy=(0, 0.5),
            xycoords='axes fraction',
            xytext=(0.2, 0.5),
            bbox=bbox_props,
            arrowprops=
                dict(facecolor='black', shrink=0.05),
                horizontalalignment='left',
                verticalalignment='center')


# third annotation relative to the figure window
bbox_props = dict(boxstyle="larrow,pad=0.5", fc="w", ec="k", lw=2)


ax.annotate('outside the plot \n relative to figure window',
            xy=(20, 75),
            xycoords='figure pixels',
            horizontalalignment='left',
            verticalalignment='top',
            bbox=bbox_props)


ax.set_xlim(-5,5)
ax.set_ylim(-1,10)
ax.set_title('Parabolic Function with Text Notation')


plt.show()