#!/bin/python
# -*- coding: utf-8 -*-

import sys

def write_col(raw_lines, col_num, filename):
    col = [line.split()[col_num] + "\n" for line in raw_lines]
    with open(filename, "w", encoding="utf-8") as write:
        write.writelines(col)

with open(sys.argv[1], "r", encoding="utf-8") as f:
    lines = f.readlines()

write_col(lines, 0, "col1.txt")
write_col(lines, 1, "col2.txt")
