from urllib.request import urlopen
from bs4 import BeautifulSoup
from requests import HTTPError

try :
    html = urlopen("http://www.pythonscraping.com/pages/page1.html")
    if html is None:
        print("URL NOT FOUND")
    else:
        print("URL FOUND")
except HTTPError as e:
    print(e)

else:
    bsObj = BeautifulSoup(html.read(), "html.parser")
    print(bsObj.div)
