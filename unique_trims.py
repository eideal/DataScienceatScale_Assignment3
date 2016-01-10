import MapReduce
import sys

"""
Assignment 3, Problem 5
Trimming Nucleotide Sequences in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

def mapper(record):
    # key: sequence ID
    # value: nucleotide sequence
    seqs = []
    seqs.append((record[1])[:-10])

    # Get unique sequences
    seq_set = set(seqs)
    for s in seq_set:
        mr.emit_intermediate(s, 1) # the 1 is meaningless since we only care about the sequence

def reducer(seq, meaningless):
    # returns unique sequences
    mr.emit(seq)


if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
