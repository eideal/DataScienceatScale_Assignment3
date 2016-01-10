import MapReduce
import sys

"""
Assignment 3, Problem 2
Implementing a relational join as a MapReduce Query
in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

def mapper(record):
    # key: order_id
    # value: an entire record from the order table or the line_item table
    orderid = record[1]

    # Return (key, value) = (order_id, record)
    mr.emit_intermediate(orderid, record)

def reducer(orderid, records):
    # returns combined records

    # Identify the order record
    for r in records:
      if r[0] == 'order':
        o_list = records.pop(records.index(r))
        break
    # Append each line_item record to the unique order record
    for r in records:
      mr.emit(o_list + r)


if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
