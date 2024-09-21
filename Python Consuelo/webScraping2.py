from bs4 import BeautifulSoup
import requests

# URL para scraping de filmes populares de um ano específico no IMDb
year = 2022
url = 'https://www.empireonline.com/movies/features/best-movies-century/'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extraindo títulos de filmes
h3_tags = soup.find_all('h3')

for tag in h3_tags:
    print(tag.text)
#print(soup)
