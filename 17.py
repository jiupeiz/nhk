#!/bin/python
# -*- coding: utf-8 -*-

import sys

with open(sys.argv[1], "r", encoding="utf-8") as f:
    lines = [line.split()[int(sys.argv[2]) - 1] for line in f.readlines()]
    print(set(lines))
