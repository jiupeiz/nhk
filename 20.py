#!/bin/python
# -*- coding: utf-8 -*-

import sys
import json

def get_country_text(filename, country_name):
    for line in open(filename):
        raw_line = json.loads(line)
        if raw_line['title'] == country_name:
            return raw_line['text']

# print(get_country_text('jawiki-country.json', u'イギリス'))

with open("uk.txt", "w", encoding="utf-8") as f:
    f.writelines(get_country_text("jawiki-country.json", u'イギリス'))
