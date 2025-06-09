# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")
# print(netflix_df)

if "decade" not in netflix_df.columns:
    netflix_df["decade"] = (netflix_df["release_year"] // 10) * 10

# Start coding here! Use as many cells as you like
movies_1990s = netflix_df[(netflix_df["decade"] == 1990)]
duration = int(movies_1990s['duration'].mode()[0]) #mode() gives most frequent values.
# print(duration)
short_action_movies = movies_1990s[(movies_1990s['duration'] < 90) & (movies_1990s['genre'] == 'Action')]
# print(short_action_movies['duration'])
short_movie_count = len(short_action_movies)
print(short_movie_count)