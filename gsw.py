#!/bin/python
# -*- coding: utf-8 -*-

from gmi import get_morphs_info
from collections import Counter


def get_sorted_word(docu):
    bags = [word["word"] for sent in docu for word in sent]
    return Counter(bags).most_common()


if __name__ == '__main__':
    docu = get_morphs_info("./neko.txt.mecab")
    result = get_sorted_word(docu)
    print(result)
