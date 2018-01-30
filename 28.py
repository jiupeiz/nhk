#!/bin/python
# -*- coding: utf-8 -*-

from gct import get_country_text
from gtv import get_template_value
import re

country_text = get_country_text("jawiki-country.json", u"イギリス")
tps_val = get_template_value(country_text)

for k, v in tps_val.items():
    plant_val = re.sub(r"'{2,5}", r"", v)
    plant_val = re.sub(r"\[{2}(.*?)\]{2}", r"\1", plant_val)
    plant_val = re.sub(r"\{{2}(.*?)\}{2}", r"\1", plant_val)
    plant_val = re.sub(r"\(.*?\)", r"", plant_val)
    plant_val = re.sub(r"<.*?>", r"", plant_val)
    plant_val = re.sub(r"\[.*?\]", r"", plant_val)
    print(k + "\t" + plant_val)
