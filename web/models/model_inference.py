import pickle
from sklearn import neighbors
from sklearn.neighbors import NearestNeighbors

# Mapping from row position to MAL ID
# .get_loc(mal_id) -> row position
# [row_position] -> mal_id
with open('models/movies_index.pkl', 'rb') as f:
  anime_index = pickle.load(f)

# Load UserAnime sparse matrix
with open('models/user_anime_pivot.pkl', 'rb') as f:
  features_matrix = pickle.load(f)

# Initialize and train a kNN model (gonna be fast)
print('Training kNN...')
model_knn = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=21, n_jobs=-1)
model_knn.fit(features_matrix)
print('kNN training completed')

def recommend_anime(mal_id: str):
  """
  Return MAL ID of top 20 recommended anime
  """
  # Get anime feature row
  mal_id = int(mal_id)
  matrix_idx = anime_index.get_loc(mal_id)
  anime_features = features_matrix[matrix_idx, :]

  # Inferrence
  neighbors = model_knn.kneighbors(anime_features, return_distance=False)

  # Convert back to MAL ID
  mal_ids = anime_index[neighbors.ravel()]
  
  # Remove original anime
  mal_ids = [i for i in mal_ids if i != mal_id]

  return mal_ids