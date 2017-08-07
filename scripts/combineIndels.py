#!/usr/bin/env python

import argparse
from collections import defaultdict
from Bio import AlignIO


def get_args():
    parser = argparse.ArgumentParser(
        description='Combines indels in of the same type/gene')
    parser.add_argument(
        "annotation",
        help="Text file with indel annotation info",
        type=argparse.FileType('r'))
    parser.add_argument("alignment", help="Indel Alignment",
                        type=argparse.FileType('r'))
    return parser.parse_args()


def parse_annotations(annotationFile):
    indels = defaultdict(list)
    for i, line in enumerate(annotationFile):
        line = line.strip().split()
        indels[(line[2], line[1].split('&')[0])].append(i)
    return indels


def merge_alignment(alignment, indels):
    align = AlignIO.read(alignment, "fasta")
    inds = list(indels.keys())
    new_align = align[:, indels[inds[0]][0]:indels[inds[0]][0]+1]
    for index in indels[inds[0]][1:]:
        for i, char in enumerate(align[:, index]):
            if char == '1':
                new_align[i].seq = "".join(list(new_align[i].seq)[:-1] + ['1'])
    for j, indel in enumerate(inds[1:]):
        new_align = new_align + align[:, indels[indel][0]:indels[indel][0]+1]
        for index in indels[indel][1:]:
            for i, char in enumerate(align[:, index]):
                if char == '1':
                    new_align[i].seq = "".join(list(new_align[i].seq)[:-1] + ['1'])
    AlignIO.write(new_align, "indels_merged.fasta", "fasta")
    with open("merged_indels_description.txt", "w") as outfile:
        for k, indel in enumerate(inds):
            outfile.write("{0}\t{1}\t{2}\n".format(str(k), indel[0], indel[1]))


args = get_args()
indels = parse_annotations(args.annotation)
merge_alignment(args.alignment, indels)
