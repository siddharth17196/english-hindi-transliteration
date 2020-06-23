import requests
from bs4 import BeautifulSoup as soup
import pickle

n = 'https://www.utf8-chartable.de/unicode-utf8-table.pl?start=2304&number=128&names=-&utf8=string-literal'
encode = {}
s = requests.Session()
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'} #bot protection

nt_all = s.get(n, headers=headers)
so = soup(nt_all.content, 'html.parser')
tab = so.find('table',{"class":"codetable"})
char = tab.find_all('td',{"class":"char"})
utf = tab.find_all('td',{"class":"utf8"})

for i in range(len(char)):
	encode[utf[i].get_text()] = char[i].get_text()

with open('encode.pkl','wb') as f:
	pickle.dump(encode, f)
