#!/bin/python
# -*- coding: utf-8 -*-

from gmi import get_morphs_info


def get_A_no_B(docu):
    result = list()
    for sent in docu:
        for i in range(1, len(sent) - 1):
            if sent[i - 1]["pos"] == "名詞" and sent[i]["word"] == "の" \
               and sent[i + 1]["pos"] == "名詞":
                phrase = "".join([sent[i - 1]["word"], sent[i]["word"],\
                                 sent[i + 1]["word"]])
                result.append(phrase)
    return set(result)


if __name__ == '__main__':
    docu = get_morphs_info("./neko.txt.mecab")
    result = get_A_no_B(docu)
    print(result)
