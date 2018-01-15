#!/bin/python
# -*- coding: utf-8 -*-

from ng import ngram
X = set(ngram("paraparaparadise",2))
Y = set(ngram("paragraph",2))
print(X)
print(Y)
print(X.union(Y))
print(X.intersection(Y))
print(X.difference(Y))
