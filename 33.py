#!/bin/python
# -*- coding: utf-8 -*-

from gmi import get_morphs_info


def get_sa_verb(docu):
    pool = list()
    for sent in docu:
        for word in sent:
            if word["pos"] == "名詞" and word["pos1"] == "サ変接続":
                pool.append(word["base"])
    return set(pool)


if __name__ == '__main__':
    docu = get_morphs_info("./neko.txt.mecab")
    verb = get_sa_verb(docu)
    print(verb)
