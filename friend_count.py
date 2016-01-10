import MapReduce
import sys

"""
Assignment 3, Problem 3
Social Network Friend Count in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

def mapper(record):
    # key: first person in record
    # value: return 1 for each record
    person = record[0]

    # Return (key, value) = (person, 1)
    mr.emit_intermediate(person, 1)

def reducer(person, counts):
    # key: person
    # value: total friend count

    # Return total friends counts for each person
      mr.emit((person, sum(counts)))


if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
