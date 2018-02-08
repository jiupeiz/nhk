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


class Chunk:
    def __init__(self):
        self.morphs = []
        # morphs is a list of Morph objects
        self.srcs = []
        self.dst = -1

    def __str__(self):
        return '{}\tsrcs: {}\tdst: [{}]'\
                .format(''.join([morph.surface for morph in self.morphs]),
                        self.srcs, self.dst)


def get_chunks(filename):
    chunks = dict()
    docu = list()
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith('*'):
                chunk_info = line.strip().split()
                idx = int(chunk_info[1])
                dst = int(chunk_info[2][:-1])

                if idx not in chunks:
                    chunks[idx] = Chunk()
                chunks[idx].dst = dst

                if dst != -1:
                    if dst not in chunks:
                        chunks[dst] = Chunk()
                    chunks[dst].srcs.append(idx)

            elif line.startswith('EOS'):
                if len(chunks) > 0:
                    sorted_chunks = sorted(chunks.items(), key=lambda x: x[0])
                    sent = list(zip(*sorted_chunks))[1]
                    docu.append(sent)
                    chunks = dict()
            else:
                word, info = line.split('\t')
                morphs = info.strip().split(',')
                chunks[idx].morphs.append(
                    Morph(word, morphs[6], morphs[0], morphs[1]))
    return docu
