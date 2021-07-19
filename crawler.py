import requests
from bs4 import BeautifulSoup


url = 'http://www.itunescharts.net/us/charts/songs/current/' 

response = requests.get(url)

html = response.content
page = BeautifulSoup(html, 'html.parser')

chart = page.find('ul', {"id":"chart"})
# print(chart) # To check the structure of the page and to see in which element the data we want is located.

# TESTING FOR ONE SONG ONLY
# n1 = page.find('li', {'id':'chart_us_songs_1'})
# print(n1)
# rank = n1.find('span', {'class':'no'})
# artist_name = n1.find('span', {'class':'artist'})
# print("Artist: ", artist_name.string)
# print("Rank: ", rank.string)
# print("Song title: ", n1.a.string)

filename = '//home/turi/git/webscrape/Songs.csv'
fp = open(filename, 'w')

song_list = chart.find_all('li')
print("\nRank Artist name\tSong Title")
fp.write("Rank, Artist name, Song Title\n")
for song in song_list:
    # print("\n", songs, "\n")
    rank = song.find("span", {"class":"no"})
    song_rank = rank.string
    name = song.find("span", {"class":"artist"})
    artist_name = name.string
    song_title = song.a.string
    print(song_rank,artist_name,"\t",song_title)
    fp.write(song_rank+","+artist_name+","+song_title+"\n")

fp.close()
