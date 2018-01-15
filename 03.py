#!/bin/python
# -*- coding: utf-8 -*-

str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
print([len(word.translate(word.maketrans({'.':None, ',':None}))) for word in str.split()])
