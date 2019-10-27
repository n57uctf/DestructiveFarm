#!/usr/bin/env python3
import sys

import redis

with redis.Redis(host=sys.argv[1], port=6379, db=0) as r:
    keys = r.keys()  # list all keys
    for key in keys:
        print(r.get(key))  # value by key
