from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
symbolfile = open("symbol.txt")
symbolslist =symbolfile.read() # ["AAPL", "SPY", "GOOG", "NFLX"]

newsymbolslist = symbolslist.split("\n")

i = 0
while i < len(newsymbolslist):
    url = "http://finance.yahoo.com/q?s=" + symbolslist[i] + "&ql=1"
    htmlfile = urlopen(url)
    htmltext = htmlfile.read()
    regex = b'<span id="yfs_184_[^.]*">(.+?)</span>'
    pattern = re.compile(regex)
    price = re.findall(pattern, htmltext)
    print("the price of", newsymbolslist[i], " is ", price)
    i += 1
