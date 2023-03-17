#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor 
from sklearn.ensemble import RandomForestClassifier
# from xgboost import XGBClassifier
import xgboost as xg

# In[5]:


df = pd.read_csv('Responses.csv')


# In[6]:


le = LabelEncoder()


# In[7]:


df.info()


# In[9]:


df.isnull().sum()


# In[10]:


df_cleaned = df.dropna(axis = 1)


# In[11]:


for column in df_cleaned.columns:
    df_cleaned[column] = le.fit_transform(df[column])


# In[12]:


df_cleaned


# In[14]:


df_cleaned.info()
# df.isnull().sum()


# In[19]:


X = df_cleaned.drop(columns = ['age_range','career_1', 'career_2',
       'career_3'])
y = df_cleaned[['career_1'
#                 , 'career_2',
#        'career_3'
               ]]


# In[20]:


X_train, X_test, y_train, y_test = train_test_split(X, y ,test_size=0.20, random_state=42)


# In[21]:


dtree = DecisionTreeClassifier(random_state=1)
dtree = dtree.fit(X_train, y_train)

y_pred = dtree.predict(X_test)
cm = confusion_matrix(y_test,y_pred)
accuracy = accuracy_score(y_test,y_pred)
print("confusion matrics=",cm)
print("  ")
print("accuracy=",accuracy*10)


# In[ ]:




