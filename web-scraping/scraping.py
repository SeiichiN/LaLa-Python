import requests
from bs4 import BeautifulSoup

result = requests.get('https://www.shoeisha.co.jp/book/ranking')
soup = BeautifulSoup(result.text, 'html.parser')

for sec in soup.select('section'):
    print(sec)
    print('---------------------')
    if sec.select_one('h2'):
        category = sec.select_one('h2').text
        title = sec.select_one('ul').select_one('li').text
        # print(category)
        # print(title)
