import MapReduce
import sys

"""
Assignment 3, Problem 6
Matrix Multiplication in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

def mapper(record):
    # key: [i,k] element of the resulting matrix
    # value: matrix element value from 'a' or 'b'

    # Assume static C = A x B is 5x5
    # For each element in A:
    if record[0] == 'a':
        for k in range(5):
            mr.emit_intermediate((record[1], k), ('a', record[2], record[3]))

    # For each element in B:
    if record[0] == 'b':
        for i in range(5):
            mr.emit_intermediate((i, record[2]), ('b', record[1], record[3]))

    

def reducer(ele_pos, list_of_values):
    # key: matrix element position
    # value: matrix element value at that position
    i = ele_pos[0]
    k = ele_pos[1]

    # Separate elements in A and B
    A_ele = []
    B_ele = []
    for mat, j, ele_value in list_of_values:
        if mat == 'a':
            A_ele.append((j, ele_value))
        if mat == 'b':
            B_ele.append((j, ele_value))

    value = 0
    for a in range(len(A_ele)):
        for b in range(len(B_ele)):
            if A_ele[a][0] == B_ele[b][0]:
               value += (A_ele[a][1])*(B_ele[b][1])

    mr.emit((i, k, value))



if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
