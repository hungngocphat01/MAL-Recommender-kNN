#!/usr/bin/env python
# coding: utf-8

import pickle
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

print('Loading sparse dataframe...')
with open('user_anime_list_df_pivot.pkl', 'rb') as f:
    df = pickle.load(f)
df = df.fillna(0)

print('Converting to CSR matrix...')
sparse_matrix = csr_matrix(df.sparse.to_coo())


print('Persisting index and matrix to file...')
with open('movies_index.pkl', 'wb') as handle:
    pickle.dump(df.index, handle, protocol=pickle.HIGHEST_PROTOCOL)



with open('user_anime_pivot.pkl', 'wb') as handle:
    pickle.dump(sparse_matrix, handle, protocol=pickle.HIGHEST_PROTOCOL)


print('Extracting necessary columns from anime database...')
anime_df = pd.read_csv('anime_cleaned.csv.zip')
anime_df.info()


anime_df = anime_df[anime_df.anime_id.isin(df.index)]


anime_df['genre'] = anime_df['genre'].str.split(',\s+')


anime_df['image_url'] = \
    anime_df['image_url'].str.replace('myanimelist.cdn-dena.com', 'cdn.myanimelist.net', regex=False)


subset_df = anime_df[['anime_id', 'title', 'title_english', 'title_synonyms', 'image_url', 
                      'type', 'source', 'score', 'rank', 'genre', 'aired_string', 'studio']]

subset_df.to_parquet('anime_db.parquet')


