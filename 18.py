#!/bin/python
# -*- coding: utf-8 -*-

import sys

with open(sys.argv[1], "r", encoding="utf-8") as f:
    for line in sorted(f.readlines(), key=lambda x: x.split()[2], reverse=True):
        print(line.strip())

# something wrong with itemgetter() in this raw data
