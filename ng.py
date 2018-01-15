#!/bin/python
# -*- coding: utf-8 -*-

def ngram(sl, n):
    return [sl[i:i + n] for i in range(0,len(sl) - n + 1)]
