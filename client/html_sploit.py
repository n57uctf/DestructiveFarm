#!/usr/bin/env python3
import sys
import requests
from bs4 import BeautifulSoup

# дока по BS4 https://www.crummy.com/software/BeautifulSoup/bs4/doc/

try:
    s = requests.session()

    response = s.get('http://' + sys.argv[1] + ':9999/list/', timeout=(5, 5))

    bs = BeautifulSoup(response.text)

    # найти все div'ы с клвсса list
    data = bs.findAll('div', {"class": "list"})

    # найти все элементы с классом "flag"
    data = bs.find(id="flag")

    # Получает весь текст без тегов, удобно, если приходится парсить регулярками
    data = bs.getText()

    print(data)

except:
    print('error')
