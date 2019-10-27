#!/usr/bin/env python3
import sys

from pymongo import MongoClient

with MongoClient(sys.argv[1], 27017) as client:
    db = client['database']
    collection = db['collection']
    # Тут наверное коллекция - аналог таблицы, тогда
    collection.find({})  # Находит всё, надо уточнить использование
