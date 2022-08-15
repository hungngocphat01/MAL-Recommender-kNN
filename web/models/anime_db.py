import pandas as pd 

anime_df = pd.read_parquet('models/anime_db.parquet')

def get_anime(mal_id):
  mal_id = int(mal_id)
  return anime_df[anime_df.anime_id == mal_id].iloc[0, :]

def get_animes(mal_ids):
  return anime_df.set_index('anime_id').loc[mal_ids, :]

def search_anime(query_string: str):
  query_string = query_string.lower()
  query_df = anime_df[
    anime_df['title'].str.lower().str.contains(query_string) |
    anime_df['title_english'].str.lower().str.contains(query_string) |
    anime_df['title_synonyms'].str.lower().str.contains(query_string)
  ]
  return query_df.sort_values('rank', ascending=True)