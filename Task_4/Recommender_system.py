import pandas as pd

ratings = pd.read_csv('C:/Users/LENOVO/Desktop/VS_Workspace/PYTHON/ratings.csv')
movies = pd.read_csv('C:/Users/LENOVO/Desktop/VS_Workspace/PYTHON/movies.csv')

# print(movies)
# print(ratings)

df = pd.merge(movies, ratings, on = "movieId")

df = df[["movieId", "title", "rating"]]

rating_count = df.groupby("title").size()
popular = rating_count[rating_count > 50].index
