import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
data = response.text

top_100 = []
soup = BeautifulSoup(data, "html.parser")
print(soup.title)
movies = [movie.getText() for movie in soup.find_all(name="h3", class_="title")]
movies = movies[::-1]
print(movies)
with open("movies.txt", "w") as file:
    for movie in movies:
        file.write(f"{movie}\n")

