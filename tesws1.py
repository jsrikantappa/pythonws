import urllib.request
import urllib.parse

#url = 'http://www.jabong.com/women/clothing/'
#http://www.imdb.com/search/title?release_date=2014,2015-01-01&title_type=feature&user_rating=1.0,10
#test_url = urllib.request.urlopen(url)
#readhtml = test_url.read()
#print (readhtml)
'''
url = 'http://pythonprogramming.net'
values = {'s' : 'clothing','search' : 'shoes'}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)
respData = resp.read()

print(respData)
'''
try:
	x = urllib.request.urlopen('https://www.google.com/search?q=test')
	print(x.read())
	
except Exception as e:
	print (str(e))
	
	
try:
	url = 'http://www.jabong.com/women/shoes/'
	headers = {}
	headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
	req = urllib.request.Request(url, headers=headers)
	resp = urllib.request.urlopen(req)
	respData = resp.read()
	
	saveFile = open('withHeaders.txt','w')
	saveFile.write(str(respData))
	saveFile.close()
	
except Exception as e:
	print (str(e))