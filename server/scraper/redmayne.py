from bs4 import BeautifulSoup
import urllib2

url = "http://www.redmayne.co.uk/research/ftse100-risersfallers.htm"

def scrape():
    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content)
    table = soup.find_all("table", class_="mainrfdata")
    rows = table[0].find_all('tr')
    indexes = []
    for row in rows:
        data = row.td
        if data != None:
            href = data.a['href']
            i = href.find('=')+1
            indexes.append(str(href[i:]))
    return indexes