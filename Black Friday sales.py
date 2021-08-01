#!/usr/bin/env python
# coding: utf-8

# # Black Friday sales 

# In[1]:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 
from collections import Counter
get_ipython().run_line_magic('matplotlib', 'inline')
import os
import warnings
warnings.filterwarnings('ignore')


# In[2]:


df = pd.read_csv(r'C:\Users\R A H U L\Desktop\test.csv')


# In[3]:


df


# # Displaying all the column names

# In[4]:


df.columns


# # Displaying the shape of the dataframe

# In[5]:


df.shape


# # Describing the dataframe

# In[6]:


df.describe()


# # Number of users by Gender

# In[7]:


df.Gender.value_counts()


# # Gender distribution

# In[8]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
genders=['Male','Female']
count_of_persons = [175772,57827]
my_explode = (0, 0.1)
my_colors = ['lightblue','silver']
ax.pie(count_of_persons, labels = genders,autopct='%1.2f%%', explode=my_explode,colors=my_colors)
plt.show()


# # Total unique values in each feature

# In[9]:


print('Unique Values for Each Feature: \n')
for i in df.columns:
    print(i, ':',df[i].nunique())


# # Total number of products and categories

# In[10]:


print('Number of products:',df['Product_ID'].nunique())
print('Number of categories:',df['Product_Category_1'].unique().max())


# # Number of Unique Items per Category

# In[11]:


plt.figure(figsize=(12,6))
prod_by_cat = df.groupby('Product_Category_1')['Product_ID'].nunique()

sns.barplot(x=prod_by_cat.index,y=prod_by_cat.values, palette="Blues_d")
plt.title('Number of Unique Items per Category')
plt.show()


# # Data types of various items

# In[12]:


df.dtypes


# # Age distribution

# In[13]:


sns.countplot(df.Age)


# # Maximum selling product in Category_1

# In[14]:


sns.countplot(df.Product_Category_1)


# # Maximum selling product in Category_2

# In[15]:


sns.countplot(df.Product_Category_2)


# # Maximum selling product in Category_3

# In[16]:


sns.countplot(df.Product_Category_3)


# # Occupation distribution

# In[17]:


sns.countplot(x='Occupation', data=df)

