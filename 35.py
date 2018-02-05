#!/bin/python
# -*- coding: utf-8 -*-

from gmi import get_morphs_info


def get_noun_seq(docu):
    result = list()
    for sent in docu:
        nouns = list()
        for word in sent:
            if word["pos"] == "名詞":
                nouns.append(word["word"])
            elif nouns:
                result.append(" ".join(nouns))
                nouns = list()
    return set(result)


if __name__ == '__main__':
    docu = get_morphs_info("./neko.txt.mecab")
    result = get_noun_seq(docu)
    print(result)
