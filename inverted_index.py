import MapReduce
import sys

"""
Assignment 3, Problem 1
Building an Inverted Index in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

def mapper(record):
    # key: document identifier
    # value: document text
    docid = record[0]
    text = record[1]
    words = text.split()

    # Get unique document words
    words_set = set(words)
    for w in words_set:
      mr.emit_intermediate(w, docid)

def reducer(key, list_of_docs):
    # key: word
    # value: list of documents word is in
    docs = []
    for v in list_of_docs:
      docs.append(v)
    mr.emit((key, docs))


if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
