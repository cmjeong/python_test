import urllib.request
from bs4 import BeautifulSoup
import codecs
import pytagcloud
import webbrowser
import matplotlib
from matplotlib import font_manager, rc
import matplotlib.pyplot as plt


def movie_reple_crowling(element_url):
    print('movie_reple_crowling function come')
    html_element = urllib.request.urlopen(element_url)
    soup_reple = BeautifulSoup(html_element, 'html.parser')
    reple_tags = soup_reple.findAll('div', attrs={'class':'score_reple'})
    for t_tag in reple_tags:
        print('-' * 50)
        print(t_tag.p.string)
#        print(tag.p)


url = "http://movie.naver.com/movie/sdb/rank/rmovie.nhn"

html = urllib.request.urlopen(url)

soup = BeautifulSoup(html, 'html.parser')

tags = soup.findAll('div', attrs={'class':'tit3'})

url_header = "https://movie.naver.com"
for tag in tags:
    element_url = url_header + tag.a['href']
    print('Movie name is : ')
    print(tag.a.string)
    print(element_url)
    movie_reple_crowling(element_url)
    print('\n\n\n\n')


# go url 
'''
for tag in reple_tags:
    print('-' * 50)
    print(tag.p)
'''
print('-' * 30)
print(tags)

