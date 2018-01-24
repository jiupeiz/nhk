#!/bin/python
# -*- coding: utf-8 -*-

import sys
from collections import Counter

with open(sys.argv[1], "r", encoding="utf-8") as f:
    cnt = Counter([line.split()[0] for line in f.readlines()])

for k, v in sorted(cnt.items(), key=lambda item: item[1], reverse=True):
    print(k)
