import urllib.request
import re

symbolslist = ["clothing","shoes","bags"]

i = 0
while i< len(symbolslist):
	urls = ["http://www.jabong.com/women/" +symbolslist[i] +"/"]
	htmlfile = urllib.request.urlopen(urls[i])
    htmltext = htmlfile.read()
	regex = '<div class="product-info"><div class="h4">(.+?) <span>(.+?)</span></div><div class="price"><span class="(.+?)"><span class="(.+?)">(.+?)</span></span><span class="(.+?)">(.+?)</span><span class="(.+?)">((.+?))</span></div>'
# '<div class="col-xxs-6 col-xs-4 col-sm-4 col-md-3 col-lg-3 product-tile img-responsive" data-product-id="(.+?)">'
	pattern = re.compile(regex)
    titles = re.findall(pattern, str(htmltext))
    print(titles)
    i+= 1

