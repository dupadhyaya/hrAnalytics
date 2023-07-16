#!/usr/bin/env python
# coding: utf-8

# ## Different Modeling Techniques
# - Continuous (eg age) - 20, 25, 22, 30.5
# - Discrete  (eg prob of selection) - Yes/No, 0/1, count of employees
# - Equation
#     - y = mx + c
#     - y = c + b1*x1 + b2 * x2
#     - y - DV, x - IV, b1, b2 - Coefficients, c - intercept
# -  Dependent variable (y)  - which depends on other variables, can be predicted
# -  Independent variable (xs) - which vary , can measure, can be changed
# 
# ### Linear Regression
# -  Predict Y (continous value) on Xs (independent variables - continous / categorical)
# 
# ### Logistic Regression
# -  Predict Y (probability of 0 or 1 ) on X (IV)
# 
# ### Decision Tree
# -  Classification Tree : like Logistic Regression
# -  Regression Tree : like Linear Regression
# 
# ### Clustering
# -  Grouping of data based on similarities 
# -  eg grouping employees based on gender, salary, et
# 
# ### Association Rule Analysis
# -  Finding association between between variables of employees
# -  Those who live more than 20 km away they prefer to work from home
# 
# ### Time Series Analysis
# -  Predict manpower requirements in next few months/ years like stock market predictions
# 
# ### Sentiment Analysis
# -  Classifying feedback into positive or negative sentiments eg. people talk positively about their dept / seniors
# 

# In[1]:


#libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pydataset import data


# ## Import Data

# In[2]:


df = data('mtcars')
df.info()


# In[3]:


df.head()


# In[8]:


df.sort_values(by='wt').plot.scatter(x='wt',y='mpg', title='Relation of wt vs mpg')
plt.show();
#as wt increases, mpg decreases ? 


# In[16]:


df.plot.scatter(x='hp',y='mpg', title='Relation of hp vs mpg')
plt.show();
#as hp increases, mpg increases ?


# In[10]:


df[['wt','mpg','hp']].corr()


# ## Linear Regression

# In[11]:


#construct a Linear Model
from sklearn.linear_model import LinearRegression


# In[20]:


reg1 = LinearRegression()


# In[13]:


df1 = df[['wt','mpg','hp']].copy()
df1.head()


# In[18]:


X = df1.drop(columns='mpg')
y = df.mpg
print(X.shape, y.shape)  #X- IV (hp, wt) DV (mpg) : Predict mpg by hp, wt


# In[21]:


reg1.fit(X,y) #run the model on X, y


# In[24]:


print('R2 ', reg1.score(X,y).round(2))
#83% of variation in Y (mpg) is dependent on X (wt, hp)


# In[25]:


print('Coefficients ', reg1.coef_)
print(X.columns)
#if u increase wt by 1 unit, mpg will decrease by 3 units (-3)
#reg1.intercept_


# In[40]:


#create new set of values
newData1 = pd.DataFrame({'wt':[3,5], 'hp':[200, 100]})
newData1


# In[27]:


print('Predict MPG for new Set of Data ', reg1.predict(newData1).round(2))


# In[ ]:


# Other advanced steps
# Train / Test Set
# Check for assumptions of Linear Regression
# Check for accuracy of model using rmse, aic
# use other libraries for developing models


# ## Logistic Regression
# -  Predict whether car is automatic or manual if you know wt, mpg, hp

# In[48]:


df2 = df[['wt','mpg','hp','am']].copy()
df2.head()


# In[49]:


from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
#seaborn to create confusion matrix


# In[51]:


X2 = df2.drop(columns = 'am')
y2 = df2.am
print('IV ', X2.shape, ' DV ', y2.shape)
print('IV ', X2.columns, ' DV ', y2.name)
print('Count of Car types \n', y2.value_counts())


# In[52]:


y2.value_counts().plot(kind='bar')
#0 - auto, 1 - manual


# In[53]:


#ogreg1 = LogisticRegression(solver='liblinear', random_state=123).fit(X,y)
logreg1 = LogisticRegression(random_state=123)
logreg1.fit(X2,y2)


# In[54]:


print(' Classes ', logreg1.classes_)
#print(' : Coeff ', logreg1.coef_, ' : Intercept ', logreg1.intercept_)
print(df2.columns)


# In[55]:


#create new set of values
newData2 = pd.DataFrame({'wt':[3,5],  'mpg':[20,25], 'hp':[200, 100]})  #same order
newData2


# In[56]:


logreg1.predict_proba(newData2)


# In[47]:


logreg1.predict(newData2)
#Manual, Auto 


# In[64]:


#confusion matrix with prediction on train data
y2_predict = logreg1.predict(X)
cm= confusion_matrix(y2, y2_predict)
print(' Confusion Matrix ', cm)
print('\nClassification Report\n', classification_report(y2, y2_predict))  #.91


# In[61]:


sns.heatmap(cm, annot=True)


# In[65]:


#advanced
#train and split data
#auc curve to select partition of prob
#AIC value to check for accurance
#p-value to select coefficients


# ## Decision Tree
# -  Predict Auto/Manual  (eg predict employee will leave or not)

# In[66]:


df3 = df[['wt','mpg','hp','carb','am']].copy()
df3.head()


# In[67]:


X3 = df3.drop(columns='am')
y3 = df2.am
print(X3.shape, y3.shape)


# In[69]:


#library
from sklearn.tree import DecisionTreeClassifier


# In[70]:


#model
clsModel = DecisionTreeClassifier(max_depth=5,random_state=123)
clsModel.fit(X3, y3)  #model with parameter


# In[72]:


clsModel.classes_  #types of values 0 or 1


# In[78]:


print(" Predicted on original Values " , clsModel.predict(X3))
print(" Original Values              " , y3.values)


# In[80]:


cm3 = confusion_matrix(y3, clsModel.predict(X3))
sns.heatmap(cm3, annot=True)
#good accuracy of the model


# In[81]:


#create new set of values
newData3 = pd.DataFrame({'wt':[3,5],  'mpg':[20,25], 'hp':[200, 100], 'carb':[4,3]})  #same order
newData3


# In[83]:


clsModel.predict(newData3)
#Manual , Auto


# ### Plot the decision tree

# In[84]:


from graphviz import Source
from sklearn import tree


# In[85]:


tree.plot_tree(decision_tree=clsModel)


# In[90]:


plt.figure(figsize=(10,7))
tree.plot_tree(clsModel, filled=True, feature_names=['wt', 'mpg', 'hp','carb'], class_names=['auto','manual'], fontsize=12, max_depth=2)
plt.title("Decision tree trained on all the Car Featurs features Predict Auto or Manual")
plt.show();


# In[91]:


# advanced
# train / Test Set
# regression Tree
# accuracy using classification score, confusion matrix, rmse
# plot tree to undersand better
# tune hyper parameters - gini, entropy, depth, 


# ## Clustering
# - grouping of data into smaller clusters which are homogenous within themselves

# In[92]:


df4 = df[['am','mpg','wt','hp','gear']].copy()
df4.head()


# In[94]:


# libraries
from sklearn.cluster import KMeans


# In[95]:


#model
kmeans = KMeans(init="random", n_clusters=3, n_init=10, max_iter=300, random_state=123)
kmeans.fit(df4)


# In[97]:


print('Final locations of the centroid' )
np.round(kmeans.cluster_centers_)   #these scaled values of   df[['am','mpg','wt','hp','gear']]


# In[100]:


kmeans.predict(df4)


# In[ ]:


df4['cluster'] = kmeans.predict(df4)


# In[106]:


df4.sort_values(by='cluster')


# In[107]:


df4.groupby('cluster').agg({'mpg':[np.mean, np.std], 'hp':[np.std, np.max], 'wt':[np.mean, np.std]})


# In[ ]:


# advanced
# hlclust
# optimal no of clusters - check by knee locator


# ## WordCloud

# In[142]:


countries = {'India','Australia','Germany','USA','Russia', 'China', 'India', 'Poland', 'Spain', 'Canada', 'Italy', 'Japan','Vulgar'}
', '.join(list(countries))


# In[143]:


univ = np.random.randint(20, 200, len(countries))
univ


# In[144]:


df6 = pd.DataFrame({'country':list(countries), 'universities':univ})
df6.head()


# In[155]:


df6.sort_values(by='universities', ascending=False)


# In[145]:


#library
from wordcloud import WordCloud, STOPWORDS


# In[146]:


tuples1 = [ tuple(x) for x in df6.values]
tuples1
#words.to_dict()


# In[147]:


dictWords = {}
for key, val in tuples1:    dictWords.setdefault(key, val)
print(dictWords)


# In[151]:


#model
wcF1 = WordCloud(scale=.8, prefer_horizontal=.5, font_step=2, min_font_size=10, max_font_size=100, \
                 include_numbers = True, background_color="white", stopwords=['Vulgar'])


# In[152]:


wcF1.generate_from_frequencies(frequencies=dictWords)
wcF1


# In[153]:


#show plot
plt.figure(figsize=(10,7))
plt.imshow(wcF1, interpolation="bilinear")
plt.axis("off")
plt.show();


# In[159]:


#word cloud from text
pmText = " Today, all Indians in the country and also abroad are celebrating the festival of independence. On this day of sacred festival of independence, the prime servant of India extends greetings to all dear countrymen.I am present amidst you not as the Prime Minister, but as the Prime Servant. The freedom struggle was fought for so many years, so many generations laid down their lives, innumerable people sacrificed their lives and youth, spent their entire lives behind bars. Today, I pay my respect, greetings and homage to all those who laid their lives for the country's independence. I also pay my respects to the crores of citizens of this country on the pious occasion of India's independence, and recall all those martyrs who had laid down their lives in India's struggle for freedom. The day of independence is a festival when we take a solemn pledge of working for the welfare of mother India, and also for the welfare of the poor, oppressed, dalits, the exploited & the backward people of our country.  My dear countrymen, a national festival is an occasion to refine and rebuild the national character. This National festival inspires us to resolve ourselves to lead a life where our character gets refined further, to dedicate ourselves to the nation and our every activity is linked to the interest of the nation and only then this festival of freedom can be a festival of inspiration to take India to newer heights."


# In[160]:


len(pmText)


# In[ ]:


counts = WordCloud().process_text(pmText)
sorted(counts.items())[1:5]


# In[161]:


wc2 = WordCloud(colormap='coolwarm').generate(pmText)
wc2


# In[163]:


plt.figure(figsize=(10,7))
plt.imshow(wc2)
plt.axis('off')
plt.show();


# In[164]:


# advance word cloud 
# sentiment analysis
# shape of image
# different methods & options


# ## Time Series
# -  Plot, predict 

# In[165]:


# datasets in pydataset
data()


# In[180]:


df7 = pd.read_csv('../data/misc/AirPassengers.csv')
df7.head()


# In[186]:


df7.columns = ['month','passengers']
df7.set_index('month', inplace=True)
df7.head()


# In[190]:


plt.figure(figsize=(20,10))
plt.xlabel("Month")
plt.ylabel("Number of Air Passengers")
plt.plot(df7)
plt.show();


# In[193]:


rolmean=df7.rolling(window=6).mean()
rolstd= df7.rolling(window=6).std()
print(rolmean.head(6))
print(rolstd.head(6))


# In[194]:


plt.figure(figsize=(20,10))
actual=plt.plot(df7, color='red', label='Actual')
mean_6=plt.plot(rolmean, color='green', label='Rolling Mean') 
std_6=plt.plot(rolstd, color='black', label='Rolling Std')
plt.legend(loc='best')
plt.title('Rolling Mean & Standard Deviation')
plt.show(block=False)


# In[195]:


# advanced TS
# ARIMA forecasting
# prediction over perids
# plot stock prices


# # end here..
# -  Keep practising.. every day.. everytime bring your data to python and play with data
