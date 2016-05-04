import urllib2
from bs4 import BeautifulSoup

url = 'http://www.imdb.com/search/title?release_date=2014,2015-01-01&title_type=feature&user_rating=1.0,10'
#'http://www.jabong.com/women/clothing/'
#'http://www.imdb.com/search/title?release_date=2014,2015-01-01&title_type=feature&user_rating=1.0,10'
test_url = urllib2.urlopen(url)
readhtml = test_url.read()
test_url.close()

bs = BeautifulSoup(readhtml)
for movie in bs.find_all('td','title'):
	title = movie.find('a').contents[0]
	genres = movie.find('span','genre').findAll('a')
	genres = [g.contents[0] for g in genres]
	runtime = movie.find('span','runtime').contents[0]
	rating = movie.find('span','value').contents[0]
	print title, genres, runtime, rating
