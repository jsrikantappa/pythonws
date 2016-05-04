import urllib.request
import re

urls = ["http://www.jabong.com/all-products/?gender=Women&tt=&rank=0&qc=women"]

regex = '<div class="product-info"><div class="h4">(.+?) <span>(.+?)</span></div><div class="price"><span class="(.+?)"><span class="(.+?)">(.+?)</span></span><span class="(.+?)">(.+?)</span><span class="(.+?)">((.+?))</span></div>'
# '<div class="col-xxs-6 col-xs-4 col-sm-4 col-md-3 col-lg-3 product-tile img-responsive" data-product-id="(.+?)">'
pattern = re.compile(regex)
i = 0
while i< len(urls):
    htmlfile = urllib.request.urlopen(urls[i])
    htmltext = htmlfile.read()
    titles = re.findall(pattern, str(htmltext))
    print(titles)
    i+= 1
	
	
#http://www.jabong.com/womenmen/clothing/
#http://www.jabong.com/women/shoes/
#http://www.jabong.com/women/bags/
#http://www.jabong.com/women/accessories/sunglasses/