#!/usr/bin/env python
# coding: utf-8

# In[336]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[337]:


df=pd.read_csv('C:/Users/Hepton/Desktop/secion 12/housing2.csv - housing2.csv.csv',sep=',',encoding='utf-8')


# In[338]:


data=df


# In[339]:


data.info()


# In[340]:


data.head(10)


# In[341]:


data.corr()


# In[342]:


data.describe()


# In[343]:


data.isnull().sum()


# In[344]:


sns.heatmap(data.isnull(),cmap='viridis',cbar=True,yticklabels=False)


# # object

# In[345]:


data['households'].value_counts()


# In[346]:


data['households']=data['households'].replace("no" , np.nan)


# In[347]:


data['households'].value_counts()


# In[348]:


data.info()


# In[349]:


data['households'].value_counts()


# In[350]:


data['households']=pd.to_numeric(data['households'])


# In[351]:


data.info()


# In[352]:


from sklearn.preprocessing import LabelEncoder


# In[353]:


data['ocean_proximity']=LabelEncoder().fit_transform(data['ocean_proximity'])


# In[354]:


data['ocean_proximity'].value_counts()


# In[355]:


data['gender'].value_counts()


# In[356]:


data.replace("male",0,inplace=True)
data.replace("female",1,inplace=True)


# In[357]:


data['gender'].value_counts()


# In[358]:


data.info()


# In[359]:


data.isnull().sum()


# # null value

# In[360]:


sns.heatmap(data.isnull(),cmap='viridis',cbar=True,yticklabels=False)


# In[361]:


data['housing_median_age'].value_counts()


# In[362]:


data['housing_median_age'].describe()


# In[363]:


data['housing_median_age'].isnull().sum()


# In[364]:


data['housing_median_age']=data['housing_median_age'].fillna(data['housing_median_age'].mean())


# In[365]:


data['housing_median_age'].isnull().sum()


# In[366]:


data.info()


# In[367]:


sns.distplot(data['housing_median_age'])


# In[368]:


data.isnull().sum()


# In[369]:


data=data.dropna(subset=['population'])


# In[370]:


data.info()


# In[371]:


data.isnull().sum()


# In[372]:


data.corr()


# In[373]:


data=data.drop('gender',axis=1)


# In[374]:


data.info()


# In[375]:


data.isnull().sum()


# In[376]:


data['households'].value_counts()


# In[377]:


data['households'].describe()


# In[378]:


data['households'].unique()


# In[379]:


fill_list=data['households'].unique()
data['households']=data['households'].fillna(pd.Series(np.random.choice(fill_list,size=len(data.index))))


# In[380]:


data.isnull().sum()


# In[381]:


data['households'].describe()


# In[382]:


sns.heatmap(data.isnull(),cmap='viridis',cbar=True,yticklabels=False)


# In[383]:


data=data.dropna(subset=['households'])


# In[384]:


data.info()


# In[385]:


data.isnull().sum()


# In[386]:


fill_list=data['total_bedrooms'].unique()
data['total_bedrooms']=data['total_bedrooms'].fillna(pd.Series(np.random.choice(fill_list,size=len(data.index))))


# In[387]:


data.isnull().sum()


# In[388]:


sns.heatmap(data.isnull(),cmap='viridis',cbar=True,yticklabels=False)


# In[389]:


data['total_bedrooms'].value_counts()


# In[390]:


data['total_bedrooms'].describe()


# In[391]:


data=data.dropna(subset=['total_bedrooms'])


# In[392]:


data.info()


# In[393]:


data.isnull().sum()


# In[394]:


fill_list=data['median_income'].unique()
data['median_income']=data['median_income'].fillna(pd.Series(np.random.choice(fill_list,size=len(data.index))))


# In[395]:


data.isnull().sum()


# In[396]:


data=data.dropna(subset=['median_income'])


# In[397]:


data.isnull().sum()


# In[398]:


data.info()


# # outlier

# In[399]:


plt.figure(figsize=(10,10))
sns.boxplot(data=data)


# In[400]:


data.plot(kind='box', subplots=True,figsize=(18,15),layout=(4,3), sharex=False, sharey=False)
plt.show()


# In[401]:


plt.scatter(data['total_rooms'], data['median_house_value'], color = 'blue')


# In[402]:


plt.scatter(df2['population'], df2['median_house_value'], color = 'blue')


# In[403]:


plt.scatter(data['total_bedrooms'], data['median_house_value'], color = 'blue')


# In[404]:


plt.scatter(data['households'], data['median_house_value'], color = 'blue')


# In[405]:


plt.scatter(data['median_income'], data['median_house_value'], color = 'blue')


# In[406]:


plt.scatter(data['ocean_proximity'], data['median_house_value'], color = 'blue')


# In[407]:


print("outliers:", data[  (data['population']>11000) ] ['population'].count())


# In[408]:


data= data[data['population'] <=11000 ] 


# In[409]:


data.info()


# In[410]:


plt.scatter(data['population'], data['median_house_value'], color = 'blue')


# In[411]:


print("outliers:", data[  (data['households']>3800) ] ['households'].count())


# In[413]:


data= data[data['households'] <=3800 ] 


# In[414]:


plt.scatter(data['households'], data['median_house_value'], color = 'blue')


# In[415]:


print("outliers:", data[  (data['total_bedrooms']>4800) ] ['total_bedrooms'].count())


# In[416]:


data= data[data['total_bedrooms'] <=4800 ] 


# In[417]:


plt.scatter(data['total_bedrooms'], data['median_house_value'], color = 'blue')


# In[418]:


data.plot(kind='box', subplots=True,figsize=(18,15),layout=(4,3), sharex=False, sharey=False)
plt.show()


# In[425]:


print("outliers:", data[  (data['total_rooms']>11000) ] ['total_rooms'].count())


# In[426]:


data= data[data['total_rooms'] <=11000 ] 


# In[427]:


plt.scatter(data['total_rooms'], data['median_house_value'], color = 'blue')


# In[428]:


data.info()


# In[429]:


data.plot(kind='box', subplots=True,figsize=(18,15),layout=(4,3), sharex=False, sharey=False)
plt.show()


# In[ ]:




