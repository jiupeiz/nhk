#!/bin/python
# -*- coding: utf-8 -*-
# 
words = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace security Clause. Arthur King Can.".replace(".",'').split()

# replace() is not needed in this case because we only print two foreahead alphabets

d = {w[:2 - (i in (1,5,6,7,8,9,15,16,19))]: i for i, w in enumerate(words,1)}
print(d)
