"""To find the subdiv_id of customers with orders more than 20"""

import csv

with open('TreeOrdersSubset.csv', mode = 'r') as fyle:
    data = list(csv.reader(fyle))
    # print(type(data))
    # ord_count = {}
    # for k, v in data:
    #     if k not in ord_count:
    #         ord_count[k] = int(v)
    #     else:
    #         ord_count[k] += int(v)

    # ord_count = {k: ord_count[k] + int(v) for k, v in data if (k not in ord_count) k : int(v) else} 
    ord_count = {}
    ord_count = {k: ord_count.get(k,int(v)) + int(v) for k, v in data}
    print(ord_count, len(ord_count))

    # print(ord_count,'\n')
    # print({k:v for k, v in ord_count.items() if v >= 20}) # dict. comprehension w/ condition.