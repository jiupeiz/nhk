#!/bin/python
# -*- coding: utf-8 -*-

from collections import Counter


def get_sorted_word(docu):
    bags = [word["word"] for sent in docu for word in sent]
    return Counter(bags).most_common()
