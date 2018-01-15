#!/bin/python
# -*- coding: utf-8 -*-

s = "I am an NLPer"
# ls = s.split()
# print([s[i:i+2] for i in range(0, len(s) - 1)])
# print([ls[i:i+2] for i in range(0, len(ls) - 1)])

def ngram(sl, n):
    return [sl[i:i + n] for i in range(0,len(sl) - n + 1)]

print(ngram(s,2))
print(ngram(s.split(),2))
