import pandas as pd

diretorio = "16k_Movies.csv"

df = pd.read_csv(diretorio)

api_key = "d90c32b085b4cb92bcac3d5bd6d92ae2"
urlBase = "https://api.themoviedb.org/3"

print(df.head())

df = df.drop(["Release Date","Description", "Rating", "No of Persons Voted", "Directed by", "Written by", "Duration", "Genres"], axis=1)

print(df.head())

df.to_csv("titulos.csv", index = False)