#!/bin/python
# -*- coding: utf-8 -*-

import re
from gct import get_country_text

lines = get_country_text("jawiki-country.json", u"イギリス").split("\n")

for line in lines:
    file_line = re.search(r"(File|ファイル)\:(.*?\.\w\w\w\w?)\|", line)
    if file_line is not None:
        print(file_line.group(2))
