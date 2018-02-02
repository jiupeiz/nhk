#!/bin/python
# -*- coding: utf-8 -*-

from gmi import get_morphs_info


def get_verb_base(docu):
    pool = list()
    for sent in docu:
        for word in sent:
            if word["pos"] == "動詞":
                pool.append(word["base"])
    return set(pool)


if __name__ == '__main__':
    docu = get_morphs_info("./neko.txt.mecab")
    verb = get_verb_base(docu)
    print(verb)
