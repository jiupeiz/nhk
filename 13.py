#!/bin/python
# -*- coding: utf-8 -*-

import sys

with open(sys.argv[1], "r", encoding="utf-8") as f1, open(sys.argv[2], "r", encoding="utf-8") as f2:
    line1, line2 = f1.readlines(), f2.readlines()

with open("merge.txt", "w", encoding="utf-8") as write:
     write.writelines("\n".join(["\t".join([col1.rstrip(), col2.rstrip()]) \
                                 for col1, col2 in zip(line1, line2)]))
