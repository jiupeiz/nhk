#!/bin/python
# -*- coding: utf-8 -*-

from gmi import get_morphs_info
from gsw import get_sorted_word
import matplotlib.pyplot as plt


def main(fq):
    len_fq = len(fq)

    plt.scatter(range(1, len_fq + 1), fq, marker='.')
    plt.xlim(1, len_fq + 1)
    plt.ylim(1, fq[0])
    plt.xscale('log')
    plt.yscale('log')
    plt.title("Zipf Rules")
    plt.xlabel("Seq of frequency")
    plt.ylabel("Frequency")

    plt.show()


if __name__ == '__main__':
    docu = get_morphs_info("./neko.txt.mecab")
    sorted_words = get_sorted_word(docu)
    fq = [sorted_words[i][1] for i in range(len(sorted_words))]
    main(fq)
