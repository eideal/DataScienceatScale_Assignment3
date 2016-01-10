import MapReduce
import sys

"""
Assignment 3, Problem 4
Determining Asymmetric Friendships in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

def mapper(record):
    # key: first person in record
    # value: return 1 for each record
    person = record[0]
    friend = record[1]

    # Define key as e.g. 'PersonA PersonB'
    person_friend = ' '.join(sorted([person, friend]))

    # Return (key, value) = (person_friend string, 1)
    mr.emit_intermediate(person_friend, 1)

def reducer(person_friend, counts):
    # return lists e.g. ['PersonA', 'PersonB'] if the relationship is asymmetric

    # If the relationship is asymmetric, sum(counts) = 1, if symmetric = 2
    if sum(counts) == 1:
        # Return e.g. ('PersonA', 'PersonB')
        mr.emit(tuple(person_friend.split()))

        # Then return ('PersonB', 'PersonA')
        split_pf = person_friend.split()
        split_pf.reverse()
        mr.emit(tuple(split_pf))


if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
