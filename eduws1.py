from bs4 import BeautifulSoup
soup = BeautifulSoup(open("G:\E\studies\python\pratice python\webscrapping\edureka\eduws.html"),"html.parser")
#print (soup.prettify())
#print (soup.html.body.contents[1])
#print (soup.html.body.contents)
#print (soup.html.body)
#print (soup.html.title)
#print (soup.get_text(''))
#print (soup.get_text('|',strip=True))
print (soup.find_all('p') [1])


