#!/bin/python
# -*- coding: utf-8 -*-

from gct import get_country_text


def get_template_value(country_text):
    lines = country_text.strip().split("\n}}\n")[0].split("\n")
    tps = [line.strip() for line in lines if line.startswith("|")]
    d = dict([tuple(line.split("<ref")[0].replace("|", "")\
                   .split(" = ")) for line in tps])
    return d


if __name__ == '__main__':
    country_text = get_country_text("jawiki-country.json", u"イギリス")
    tps_val = get_template_value(country_text)
    print(tps_val)
