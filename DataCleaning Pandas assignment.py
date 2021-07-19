#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN',
'londON_StockhOlm',
'Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})


# In[2]:


df


# In[3]:



n= df.loc[df['FlightNumber'].isna()]
n


# # 1. NaN values in FlightNumber column meant to increase by 10 with each row so 10055 and 10075 need to be put in place. Fill in these missing numbers and make the column an integer column(instead of a float column).

# In[5]:


df['FlightNumber'].interpolate(method ='linear', limit_direction ='forward',downcast='int',inplace=True)


# In[6]:


df


# In[6]:


df['From_To'].dtype


# In[7]:


df['From_To']


# # 2. The From_To column Split each string on the underscore delimiter _ to give a new temporary DataFrame with the correct values. Assign the correct column names to this temporary DataFrame.

# In[8]:


new = df['From_To'].str.split('_',n=2,expand=True)
df['From']=new[0]
df['To']=new[1]


# In[9]:


df


# # 4. Delete the From_To column from df and attach the temporary DataFrame from the previous questions.

# In[10]:


df.drop(columns='From_To',inplace=True)


# In[12]:


df


# # 3. Standardise the strings so that only the first letter is uppercase (e.g. "londON" should become "London".)

# In[13]:


df['From']=df['From'].str.capitalize()


# In[14]:


df


# In[15]:


df['To']=df['To'].str.capitalize()
df


# In[16]:


df['RecentDelays']


# # 5. Expand the Series of lists into a DataFrame named delays, rename the columns delay_1, delay_2, etc. and replace the unwanted RecentDelays column in df with delays.

# In[17]:


df[['delay1','delay2','delay3']] = pd.DataFrame(df.RecentDelays.values.tolist(), index= df.index)


# In[18]:


df


# In[19]:


df.drop(columns='RecentDelays',inplace =True)
df


# In[ ]:




