import pandas as pd     #Import pandas to manipulate with the data

ratings = pd.read_csv('C:/Users/LENOVO/Desktop/VS_Workspace/PYTHON/ratings.csv')        # Read the ratings CSV file
movies = pd.read_csv('C:/Users/LENOVO/Desktop/VS_Workspace/PYTHON/movies.csv')          # Read the movies CSV file

df = pd.merge(movies, ratings, on = "movieId")          # Merge the movies and ratings dataframes on 'movieId'

user_rating_count = df.groupby("userId").size()                         # Group by userId and count the number of ratings
prolific_users = user_rating_count[user_rating_count > 100].index       # Select userId with more than 100 ratings
filtered_rating = df[df["userId"].isin(prolific_users)]                 # Filter the dataframe to include only ratings from prolific users

movie_rating_count = df.groupby("title").size()                                     # Group by title and count the number of ratings
famous_movies = movie_rating_count[movie_rating_count > 50].index                   # Select movie titles with more than 50 ratings
final_rating = filtered_rating[filtered_rating["title"].isin(famous_movies)]        # Filter the dataframe to include only famous movies

pt = final_rating.pivot_table(index = "title", columns = "userId", values = "rating")       # Create pivot table where index is title, colomns is for users and values is rating
pt.fillna(0, inplace = True)                            # replace null values with 0

print(pt)