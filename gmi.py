#!/bin/python
# -*- coding: utf-8 -*-


def get_morphs_info(filename):
    docu = list()
    sent = list()
    for line in open(filename).readlines():
        if line.startswith("EOS"):
            docu.append(sent)
            sent = list()
            continue
        word, info = line.rstrip().split("\t")
        info_list = info.split(",")
        morphs = {"word": word, "base": info_list[6], "pos": info_list[0], "pos1": info_list[1]}
        sent.append(morphs)
    return docu
