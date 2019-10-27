#!/usr/bin/env python3
import sys

import psycopg2

with psycopg2.connect(host=sys.argv[1],
                      user="default_login",
                      password="default_password",
                      dbname="service_db",
                      port=5432) as db:
    with db.cursor() as cur:
        # Делаем запрос в таблицу с флагами. Ограничено 15 последними флагами(пример)
        cur.execute("SELECT flag FROM flags ORDER BY id DESC LIMIT 15")  # Change this
        # Вернется список из кортежей вида [('1',...),('2',...)]
        result = cur.fetchall()
print(result)
