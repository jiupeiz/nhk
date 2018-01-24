#!/bin/python
# -*- coding: utf-8 -*-

from gct import get_country_text

lines = get_country_text("jawiki-country.json", u'イギリス').split("\n")

for line in lines:
    if line.startswith("[[Category:"):
        print(line)
