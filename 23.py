#!/bin/python
# -*- coding: utf-8 -*-

import re
from gct import get_country_text

lines = get_country_text("jawiki-country.json", u"イギリス").split("\n")

for line in lines:
    sec_line = re.search(r"^\=+(.*?)\=+$", line)
    if sec_line is not None:
        print("--" * int((line.count("=") / 2 - 2))\
              + str(int(line.count("=") / 2 - 1)) \
              + "\t" + sec_line.group(1))
