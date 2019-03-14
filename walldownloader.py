import urllib.request as u
import requests as re
from bs4 import BeautifulSoup
from  random import randint
qry  = str(input('Search here...'))
qry = qry.replace(' ','+')
soup = BeautifulSoup(re.get('https://wallpapercave.com/search?q='+qry).text,'html.parser')
for a in soup.find_all("a", class_ ="albumthumbnail even"):
    href= 'https://wallpapercave.com'+a.get('href')
    main = BeautifulSoup(re.get(href).text,'html.parser')
    for download in main.find_all("a",class_ ="download"):
        downloadbu ='https://wallpapercave.com'+download.get("href")
        uu =u.urlopen(downloadbu)
        datatowrite = uu.read()
        with open('img/'+str(randint(1, 10000))+'.jpg','wb') as f:
            f.write(datatowrite)            
