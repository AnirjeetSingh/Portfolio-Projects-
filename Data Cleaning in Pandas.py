#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd


# In[7]:


df = pd.read_excel(r"C:\Users\NAME\Downloads\pandas file\Customer Call List.xlsx")


# In[8]:


df


# In[10]:


df = df.drop_duplicates()
df


# In[15]:


df = df.drop(columns = 'Not_Useful_Column')
df


# In[19]:


df['Last_Name']= df['Last_Name'].str.lstrip('...')
df['Last_Name']= df['Last_Name'].str.lstrip('/')
df['Last_Name']= df['Last_Name'].str.rstrip('_')

df


# In[83]:


df = pd.read_excel(r"C:\Users\NAME\Downloads\pandas file\Customer Call List.xlsx")
df


# In[84]:


df = df.drop_duplicates()
df = df.drop(columns = 'Not_Useful_Column')
df


# In[85]:


df['Last_Name']= df['Last_Name'].str.strip('./_')
df


# In[86]:


df['Phone_Number'] = df['Phone_Number'].str.replace('[^a-zA-Z0-9]','')
df


# In[87]:


df['Phone_Number'] = df['Phone_Number'].str.replace('Na','')
df


# In[88]:


df['Phone_Number'] = df['Phone_Number'].fillna('')
df


# In[89]:


df['Address'].str.split(',',2,expand=True)


# In[90]:


df[["Street Address", "State", "Zip Code"]] = df['Address'].str.split(',',2,expand=True)


# In[91]:


df


# In[92]:


df['Paying Customer'] = df['Paying Customer'].str.replace('Yes','Y')
df['Paying Customer'] = df['Paying Customer'].str.replace('No','N')
df


# In[93]:


df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('Yes','Y')
df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('No','N')
df


# In[94]:


df = df.fillna('')
df


# In[95]:


df


# In[96]:


for x in df.index:
    if df.loc[x,'Do_Not_Contact'] == 'Y':
        df.drop(x,inplace=True)
df


# In[102]:


for x in df.index:
    if df.loc[x,'Phone_Number'] == '':
        df.drop(x,inplace=True)
df


# In[103]:


df = df.reset_index(drop=True)
df


# In[ ]:




