from time import sleep
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
z = set()
w = str()
data = []
data_boevik =[]
data_drama =[]
for p in range(1, 2):
    print(p)
    url = f"https://kinobar.vip/detektiv/page/{p}"
    r = requests.get(url)
    sleep(2)
    soup = BeautifulSoup(r.text, "lxml")
    films = soup.findAll('div', class_='main_news')

    for film in films:
        link = film.find('div', class_='mn_left_img').find('a', class_='link img').get('href')[:]
        name = film.find('h2', class_='zagolovok').text.rstrip()
        try:
            genre = film.find('ul', class_='teaser_ads').text.split('\n')[2].split(':')[1].strip()
            # genre = film.find('ul', class_='teaser_ads').text.split('\n')[2].split(',')[1].strip()
        except:
            genre = '-'
        director = film.find('div', class_='mn_text').find('li', id='teaser_rej').text.split(":")[1].strip()
        year = film.find('ul', class_='teaser_ads').text.split(':')[1].split()[0]
        appearance = film.find('ul', class_='mn_links').text.split('\n')[1]

        data.append([link, name, genre, director, year, appearance])

        if genre == 'Боевики':
            data_boevik.append([link, name, genre, director, year, appearance])
            # print("OK")
            # print('type(genre)', type(genre))
        if genre == 'Драмы':
            data_drama.append([link, name, genre, director, year, appearance])

        header = ['link', 'name', 'genre', 'director', 'year', 'appearance']
        df = pd.DataFrame(data, columns=header)
        df.to_csv('kino_parsing.csv', sep=';', encoding='utf-8')

        w = w + ', ' + genre
    print('type(genres)', type(w), w)
    string = w
    string = string.split(",")
    print('string 1 ', type(string), string)
    for i in range(len(string)):
        string[i] = string[i].strip()
    print(string)
    hi = set(string)
    hi.pop()
    hi = list(hi)
    print('hi', len(hi), type(hi), hi)

    print('type(genre)', type(genre), genre)
    # The code below is only for demonstrating the process through the terminal.

print(data)