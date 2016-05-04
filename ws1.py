import urllib.request
import re

urls = ["http://www.jabong.com/women/","http://google.com","http://youtube.com"]

regex = "<title>(.+?)</title>"
pattern = re.compile(regex)

i = 0
while i< len(urls):
    htmlfile = urllib.request.urlopen(urls[i])
    htmltext = htmlfile.read()
    titles = re.findall(pattern, str(htmltext))
    print(titles)
    i+= 1

