from time import sleep
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

z = set()
ag = str()
data = []
data_boevik =[]
data_drama =[]

url0 = f'https://kinobar.vip/'
r0 = requests.get(url0)
soup0 = BeautifulSoup(r0.text, 'lxml')


for p in range(1, 3):
    print(p)
    url = f"https://kinobar.vip/detektiv/page/{p}"
    r = requests.get(url)
    sleep(2)
    soup = BeautifulSoup(r.text, "lxml")
    films = soup.findAll('div', class_='main_news')

    for film0 in films:
        # link = film.find('div', class_='mn_left_img').find('a', class_='link img').get('href')[:]
        # name = film.find('h2', class_='zagolovok').text.rstrip()
        try:
            genre0 = film0.find('ul', class_='teaser_ads').text.split('\n')[2].split(':')[1].strip()
        except:
            genre0 = '-'
        # director = film.find('div', class_='mn_text').find('li', id='teaser_rej').text.split(":")[1].strip()
        # year = film.find('ul', class_='teaser_ads').text.split(':')[1].split()[0]
        # appearance = film.find('ul', class_='mn_links').text.split('\n')[1]

        # data.append([link, name, genre, director, year, appearance])

        # if genre == 'Боевики':
        #     data_boevik.append([link, name, genre, director, year, appearance])
        #     # print("OK")
        #     # print('type(genre)', type(genre))
        # if genre == 'Драмы':
        #     data_drama.append([link, name, genre, director, year, appearance])

        # header = ['link', 'name', 'genre', 'director', 'year', 'appearance']
        # df = pd.DataFrame(data, columns=header)
        # df.to_csv('kino_parsing.csv', sep=';', encoding='utf-8')

        ag += ', ' + genre0          # ag => variable (all genres)

print('type(ag)', type(ag), ag)

agl = ag.split(',')             # agl => variable (all genres list)
print('agl', type(agl), agl)

for i in range(len(agl)):
    agl[i] = agl[i].strip()
print(agl)

ag_set = set(agl)               # ag_set => variable (all genres set)
ag_set.pop()                    # crutch to remove first empty item in variable genre
agl_cl = list(ag_set)           # agl_cl => variable (all genres list cleaned)
print('agl_cl', len(agl_cl), type(agl_cl), agl_cl)

print('type(genre0)', type(genre0), genre0)
                                # The code below is only for demonstrating the process through the terminal.

# print('type(data)', type(data), data)
#
# print(len(data[0][2]))
# print(data[0][2])
# gs = data[0][2].split(',')      # gs => variable (genre single)
# print(gs, len(gs))
# print('len(agl_cl)', len(agl_cl))

# for n in range(len(agl_cl)):
#     if agl_cl[n] in data[0][2]:
#         # data{agl_cl[n]}.append([link, name, genre, director, year, appearance])
#
#         header = ['link', 'name', 'genre', 'director', 'year', 'appearance']
#         # dsd = dict(zip(header, data[0][:]))
#         df = pd.DataFrame(data[0][:], columns=header)
#         df.to_csv('kino_parsing'+agl_cl[n]+'.csv', sep=';', encoding='utf-8')
#
#         # print('type(dsd)', type(dsd), dsd)
#
#         print('Yes', agl_cl[n])
#         print('data[0][2]', data[0])
#     else:
#         print('No')
# print('type(data)', type(data), data)
########################################################################################################################
# for p in range(1, 3):
#     print(p)
#     url = f"https://kinobar.vip/detektiv/page/{p}"
#     r = requests.get(url)
#     sleep(2)
#     soup = BeautifulSoup(r.text, "lxml")
#     films = soup.findAll('div', class_='main_news')
#     for film in films:
#         link = film.find('div', class_='mn_left_img').find('a', class_='link img').get('href')[:]
#         name = film.find('h2', class_='zagolovok').text.rstrip()
#         try:
#             genre = film.find('ul', class_='teaser_ads').text.split('\n')[2].split(':')[1].strip()
#         except:
#             genre = '-'
#         director = film.find('div', class_='mn_text').find('li', id='teaser_rej').text.split(":")[1].strip()
#         year = film.find('ul', class_='teaser_ads').text.split(':')[1].split()[0]
#         appearance = film.find('ul', class_='mn_links').text.split('\n')[1]

        # data.append([link, name, genre, director, year, appearance])

        # if genre == 'Боевики':
        #     data_boevik.append([link, name, genre, director, year, appearance])
        #     # print("OK")
        #     # print('type(genre)', type(genre))
        # if genre == 'Драмы':
        #     data_drama.append([link, name, genre, director, year, appearance])


    # header = ['link', 'name', 'genre', 'director', 'year', 'appearance']
    # df = pd.DataFrame(data, columns=header)
    # df.to_csv('kino_parsing.csv', sep=';', encoding='utf-8')