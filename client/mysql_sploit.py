#!/usr/bin/env python3
import sys

import mysql.connector

with mysql.connector.connect(
        host=sys.argv[1],
        user="default_login",
        passwd="default_password",
        database="service_db",
        port=3306) as db:
    with db.cursor() as cur:
        # Делаем запрос в таблицу с флагами. Ограничено 15 последними флагами(пример)
        cur.execute("SELECT flag FROM flags ORDER BY id DESC LIMIT 15")  # Change this
        # Вернется список из кортежей вида [('1',...),('2',...)]
        result = cur.fetchall()
print(result)
