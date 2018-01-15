#!/bin/python
# -*- coding: utf-8 -*-

import random

def gentypo(word):
    if len(word) <= 4 : return word

    typo = list(word[1:-1])
    random.shuffle(typo)
    return word[0] + "".join(typo) + word[-1]

s = "I couldn't believe that I could actually understand what\
        I was reading : the phenomenal power of the human mind ."

print(" ".join(list(map(gentypo,(s.split())))))
