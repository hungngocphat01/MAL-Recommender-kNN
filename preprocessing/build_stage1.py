#!/usr/bin/env python
# coding: utf-8

# This notebook preprocesses the dataset and select appropriate animes to save in the final recommendation dataset.
# 
# The original UserAnime dataset has around 80M rows, so it is impossible to work it on my machine. One "dirty" workaround I came up with is to only select some animes which has high ranking to be included in the final recommender system.

# In[1]:


import gc
import pandas as pd
import numpy as np
import seaborn as sns


# # Brief analyze of the "anime list"
# 
# Just a very simple and dirty process to filter out "valueable" animes to be included in the final database

# In[2]:

print('Loading anime database...')
anime_df = pd.read_csv('anime_cleaned.csv.zip')
tvmv_df = anime_df[anime_df.type.isin(['TV', 'Movie'])]
tvmv_df = tvmv_df[~((tvmv_df['rank'] > 5000) & (tvmv_df.scored_by < tvmv_df.scored_by.quantile(0.5)))]

# # Process our big list: UserAnimeList

# **Read necessary columns to memory**

# In[9]:

print('Loading user-anime database...')
df = pd.read_csv('UserAnimeList.csv.zip', usecols=['username', 'anime_id', 'my_score'])


# In[10]:


# **Only take animes which are in the given list**

# In[11]:


print('Filtering...')
df = df[df.anime_id.isin(tvmv_df.anime_id)]

# **Each user may watch an anime multiple times, only keep the one with max score**

# In[13]:


print('Aggregating...')
df = df.groupby(['anime_id', 'username'])['my_score'].max()


# **Pivot the table**

# In[14]:

print('Pivoting...')
df_pivot = df.unstack()


# In[15]:


del df
gc.collect()

# In[18]:

print('Converting dataframe to sparse...')
pivot_sparse_df = df_pivot.astype(pd.SparseDtype('int64', np.nan))


# In[19]:


del df_pivot
gc.collect()


# In[20]:


pivot_sparse_df.index.name = None


# In[25]:

print('Saving sparse dataframe to file...')
pivot_sparse_df.to_pickle('user_anime_list_df_pivot.pkl')

