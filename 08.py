#!/bin/python
# -*- coding: utf-8 -*-

def  cipher(message):
    ret = ""
    for char in message:
        ret += chr(219 - ord(char)) if char.islower() else char
    return ret
s = "Atbash is a simple substitution cipher for the Hebrew alphabet."

print(cipher(s))
print(cipher(cipher(s)))
