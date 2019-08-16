import requests
from bs4 import BeautifulSoup

result = requests.get("http://midas.iiitd.edu.in")
src = result.content
soup = BeautifulSoup( src, 'lxml')

links = soup.find_all("a")

print(links)