#!/bin/python
# -*- coding: utf-8 -*-

from gmi import get_morphs_info
from gsw import get_sorted_word
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


def main(words, fq):
    fp = FontProperties(fname="/usr/share/fonts/TTF/meiryo.ttc")
    plt.figure()
    plt.bar(range(10), fq)
    plt.xticks(range(10), words, fontproperties=fp)
    plt.title("Top 10 appears words")
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.show()


if __name__ == '__main__':
    docu = get_morphs_info("./neko.txt.mecab")
    sorted_words = get_sorted_word(docu)
    words = [sorted_words[i][0] for i in range(10)]
    fq = [sorted_words[i][1] for i in range(10)]
    main(words, fq)
