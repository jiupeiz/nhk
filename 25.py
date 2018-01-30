#!/bin/python
# -*- coding: utf-8 -*-

from gct import get_country_text

lines = get_country_text("jawiki-country.json", u"イギリス")\
        .strip().split("\n}}\n")[0].split("\n")
tps = [line.lstrip("|") for line in lines if line.startswith("|")]

d = dict([tuple(line.split("<ref")[0].split(" = ")) for line in tps])

print(d)
