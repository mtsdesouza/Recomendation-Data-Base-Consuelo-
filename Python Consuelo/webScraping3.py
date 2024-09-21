from bs4 import BeautifulSoup
import requests

# URL para scraping de filmes populares de um ano específico no IMDb
year = 2022
url = 'https://www.cinemablend.com/movies/the-100-best-movies-of-the-1990s'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extraindo títulos de filmes
h3_tags = soup.find_all('h2')

for tag in h3_tags:
    print(tag.text)
#print(soup)
