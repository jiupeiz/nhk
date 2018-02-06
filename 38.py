#!/bin/python
# -*- coding: utf-8 -*-

from gmi import get_morphs_info
from gsw import get_sorted_word
import matplotlib.pyplot as plt
# from matplotlib.font_manager import FontProperties


def main(fq):
    # fp = FontProperties(fname="/usr/share/fonts/TTF/meiryo.ttc")
    plt.hist(fq, bins=20, range=(1, 20), align='mid')
    plt.xlim(xmin=1, xmax=20)
    plt.xticks([1, 5, 10, 15, 20])
    plt.xlabel("Freqnency")
    plt.ylabel("Types")
    plt.title("Tpyes appeared over 20 times")
    plt.grid(axis="y")
    plt.show()


if __name__ == '__main__':
    docu = get_morphs_info("./neko.txt.mecab")
    sorted_words = get_sorted_word(docu)
    fq = [sorted_words[i][1] for i in range(len(sorted_words))]
    main(fq)
