#!/usr/bin/env python3
import sys
import json
import requests

# дока по requests https://requests.kennethreitz.org/en/master/

register_data = {'username': 'user', 'password': '123123'}
headers = {'Accept': 'application/json'},

try:
    s = requests.session()

    # POST запрс c form-data
    s.post('http://' + sys.argv[1] + ':9999/api/register/', json=register_data, timeout=(5, 5))

    # GET запрос с query параметрами и заголовками
    response = s.get('http://' + sys.argv[1] + ':9999/list/', params=register_data, headers=headers, timeout=(5, 5))

    data = json.loads(response.text)
    print(data['flag'])

except:
    print('error')
