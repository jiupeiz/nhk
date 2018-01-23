#!/bin/python
# -*- coding: utf-8 -*-

import sys

with open(sys.argv[1], "r", encoding="utf-8") as f:
    lines = f.readlines()

if len(lines) % int(sys.argv[2]) != 0:
    raise Exception("Undividable by %d" % int(sys.argv[2]))
else:
    parts = int(sys.argv[2])
    line_per_part = int(len(lines) / parts)

    for i in range(parts):
        with open("part%s.txt" % str(i + 1), "w", encoding="utf-8") as w:
            w.writelines(lines[line_per_part * i : line_per_part * (i + 1)])
