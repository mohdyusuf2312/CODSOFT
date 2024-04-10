import pandas as pd     #Import pandas to manipulate with the data
import numpy as np      # Numpy has wide range of mathematical fuctions
from sklearn.metrics.pairwise import cosine_similarity      #Import cosine similarity to check similarity between movies

logo = '''
██████  ███████  ██████  ██████  ███    ███ ███    ███ ███████ ███    ██ ██████   █████  ████████ ██  ██████  ███    ██     ███████ ██    ██ ███████ ████████ ███████ ███    ███ 
██   ██ ██      ██      ██    ██ ████  ████ ████  ████ ██      ████   ██ ██   ██ ██   ██    ██    ██ ██    ██ ████   ██     ██       ██  ██  ██         ██    ██      ████  ████ 
██████  █████   ██      ██    ██ ██ ████ ██ ██ ████ ██ █████   ██ ██  ██ ██   ██ ███████    ██    ██ ██    ██ ██ ██  ██     ███████   ████   ███████    ██    █████   ██ ████ ██ 
██   ██ ██      ██      ██    ██ ██  ██  ██ ██  ██  ██ ██      ██  ██ ██ ██   ██ ██   ██    ██    ██ ██    ██ ██  ██ ██          ██    ██         ██    ██    ██      ██  ██  ██ 
██   ██ ███████  ██████  ██████  ██      ██ ██      ██ ███████ ██   ████ ██████  ██   ██    ██    ██  ██████  ██   ████     ███████    ██    ███████    ██    ███████ ██      ██ 
                                                                                                                                                                                 
'''

ratings = pd.read_csv('https://github.com/mohdyusuf2312/CODSOFT/blob/main/Task_4/ratings.csv')        # Read the ratings CSV file
movies = pd.read_csv('https://github.com/mohdyusuf2312/CODSOFT/blob/main/Task_4/movies.csv')          # Read the movies CSV file

df = pd.merge(movies, ratings, on = "movieId")          # Merge the movies and ratings dataframes on 'movieId'

user_rating_count = df.groupby("userId").size()                         # Group by userId and count the number of ratings
prolific_users = user_rating_count[user_rating_count > 100].index       # Select userId with more than 100 ratings
filtered_rating = df[df["userId"].isin(prolific_users)]                 # Filter the dataframe to include only ratings from prolific users

movie_rating_count = df.groupby("title").size()                                     # Group by title and count the number of ratings
famous_movies = movie_rating_count[movie_rating_count > 50].index                   # Select movie titles with more than 50 ratings
final_rating = filtered_rating[filtered_rating["title"].isin(famous_movies)]        # Filter the dataframe to include only famous movies

pt = final_rating.pivot_table(index = "title", columns = "userId", values = "rating")       # Create pivot table where index is title, colomns is for users and values is rating
pt.fillna(0, inplace = True)                            # replace null values with 0

similarity_score = cosine_similarity(pt)                # check cosine_similarity of pivot table and srote it into similarity_score variable

def recommend(movie_name):                              # Recommend method to recommend 5 similar movies with the help of cosine similarity score
    try:
        index = np.where(pt.index == movie_name)[0][0]      # check movie index in the data frame
    except IndexError:                                      # If movie not in movies.csv or not in (final_rating data frame)
        print("This movie is out of my knowledge or less popular")
    else:
        similar_items = sorted(list(enumerate(similarity_score[index])), key = lambda x:x[1],reverse=True)[1:6]             # check similarity with other movies, and high similar value movies are store in similar_items variable
        print(f"Here are 5 movies that are similar to {movie_name}: ")
        for i in similar_items:
            print(pt.index[i[0]])                   # print most similar movies on the basis of given movie

print(logo)
start = True
while start == True:
    user_input = input("\nEnter your movie name or type 'e' for exit : ")                # Take movie name from the user as input
    if user_input == "e" or user_input == "E":
        print("\nThank you!")
        start = False
    else:
        recommend(user_input)                                        # Send movie name to the recommend method
