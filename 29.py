#!/bin/python
# -*- coding: utf-8 -*-

from gct import get_country_text
from gtv import get_template_value
import re
import requests


def flat_json(res_json):
    flatted_json = {}
    for k, v in res_json.items():
        if isinstance(v, list):
            for e in v:
                flatted_json.update(flat_json(e))
        elif isinstance(v, dict):
            flatted_json.update(flat_json(v))
        else:
            flatted_json[k] = v
    return flatted_json



country_text = get_country_text("jawiki-country.json", u"イギリス")
tps_val = get_template_value(country_text)

d = {}

for k, v in tps_val.items():
    plant_val = re.sub(r"'{2,5}", r"", v)
    plant_val = re.sub(r"\[{2}(.*?)\]{2}", r"\1", plant_val)
    plant_val = re.sub(r"\{{2}(.*?)\}{2}", r"\1", plant_val)
    plant_val = re.sub(r"\(.*?\)", r"", plant_val)
    plant_val = re.sub(r"<.*?>", r"", plant_val)
    plant_val = re.sub(r"\[.*?\]", r"", plant_val)
    plant_val = re.sub(r"lang\|\w{2}\|", r"", plant_val)
    d[k] = plant_val

url = "https://en.wikipedia.org/w/api.php"

para = {"action": "query",
        "titles": "File:{}".format(d[u"国旗画像"]),
        "prop": "imageinfo",
        "format": "json",
        "iiprop": "url"}

res = requests.get(url, params=para).json()

print(flat_json(res)["url"])
