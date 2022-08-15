# Anime recommendation system on MAL dataset

This is my first recommendation system using collaborative filtering. For simplicity, I decided to use sklearn's `KNearestNeighbors` for this project.

Dataset used: [MyAnimeList Dataset](https://www.kaggle.com/datasets/azathoth42/myanimelist).

## Project structure
- `preprocessing`: source files and notebooks to the preprocess original dataset and build the sparse user-movies matrix.
- `web`: a simple Flask application for demonstrating the system.

## How to

1. Download the following files from the above Kaggle dataset
   - `anime_cleaned.csv.zip` 
   - `UserAnimeList.csv.zip`
2. Put them into `modeling` folder (do not extract).
3. Run `preprocessing/build.sh`.
4. After building, copy following files to `web/models/`
   - `anime_db.parquet`
   - `movies_index.pkl`
   - `user_anime_pivot.pkl`
5. Run `web/app.py`

Note: the user-anime dataset consists of around 80 million rows, so make sure that you have enough memory to run the build script. It ran fine on my laptop with 16 GB of RAM.

You should also use the same Python version to build the dataset and to serve the Flask application.

## Short demo

![demo](demo/demo.gif)
