#!/bin/python
# -*- coding: utf-8 -*-


class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return 'surface: {}\tbase: {}\tpos: {}\tpos1: {}'\
                .format(self.surface, self.base, self.pos, self.pos1)


def get_morphs(filename):
    with open(filename) as f:
        lines = f.readlines()
        sent = list()
        docu = list()
        for line in lines:
            if line.startswith('*'):
                continue
            elif line.startswith('EOS'):
                docu.append(sent)
                sent = list()
            else:
                word, info = line.split('\t')
                morphs = info.strip().split(',')
                sent.append(Morph(word, morphs[6], morphs[0], morphs[1]))
    return docu


if __name__ == '__main__':
    docu = get_morphs("./neko.txt.cabocha")
    for word in docu[2]:
        print(word)
