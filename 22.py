#!/bin/python
# -*- coding: utf-8 -*-

import re
from gct import get_country_text

lines = get_country_text("jawiki-country.json", u"イギリス").split("\n")

for line in lines:
    cat_line = re.search(r"^\[\[Category:(.*?)(|\|.*)\]\]$", line)
    if cat_line is not None:
        print(cat_line.group(1))
