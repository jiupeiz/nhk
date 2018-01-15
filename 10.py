#!/bin/python
# -*- coding: utf-8 -*-

import sys
with open(sys.argv[1]) as f:
    lines = f.readlines()

print(len(lines))
