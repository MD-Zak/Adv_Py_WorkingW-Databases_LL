import csv

with open("treeOrderssubsetnodupes.csv", mode = 'r') as inf:
    data = list(csv.reader(inf))
    # data = list(data)
    # new_dict = dict()
    new_dict = {}

    for row in data[1:]:
        keys = row[0]
        value = row[1]
        new_dict[keys] = value

    print("Total number of entries:",len(new_dict),"\n") # 1_ch1

            # print(e)
    #         pass
            # no_trees | None = int(input('Enter the number of trees to be collected:\n'))
    # no_trees = int() | None
    # no_trees = int(input('Enter the number of trees to be collected:\n'))
    # we need to firstly check if the input is indeed of type int, and then also allow the feature to accept a NoneType to skip the input.
    # trees = 0
    # trees = int(input('Enter the number of trees to be collected or 0 to skip:\n'))
"""Inputting a new int entry. #1_ch2""" 
    trees = int()
    sub_divId = int()
    try: trees = int(input('Enter the number of trees to be collected:\n'))
    except Exception as e:  
        print('//TypeError// : Enter a number \n')
        # exit() 
    try: sub_divId = int(input("Enter the sub-divison ID from where this as to be collected :\n"))
    except Exception as e: print('//TypeError// : Enter a number \n') 
    finally: 
        if trees is None: trees = 0     
        if sub_divId is None: sub_divId = 0

"""Adding the fresh values to the dict.#1_ch3 """

    if trees and sub_divId:
        new_dict[str(sub_divId)] = str(trees)
        print('New entry successfully added.')
        print(new_dict)

""" Printing the final dict. #1_ch4 """
    for keys in new_dict:
        print(keys," : ",new_dict[keys])

"""Rough work starts"""
    # def qc(some):
    #     if some is None:
    #         print('if block')
    #         return 0
        # if type(some) == None:
        #     print("if block")
        #     return 0
        # elif type(some) == str:
        #     print('elif block\n')
        #     print("//TypeError//: Enter a number" )
        #     return exit()
        # # elif some is None:
        # #     return print("elif block")
        # else: 
        #    print("else block")
        #    return exit()

    # trees = qc(input('Enter the number of trees to be collected:\n'))
    # sub_divId = qc(input("Enter the sub-divison ID from where this as to be collected:\n"))

    # try: 
    #     trees = int(input('Enter the number of trees to be collected:\n'))
    # except Exception as e:
    #     if e is str:
    #         print('//TypeError// : Enter a number \n')
    #         exit()
        # else:
        #     qc(e)
    # try: sub_divId = qc(int(input("Enter the sub-divison ID from where this as to be collected:\n")))
    # except Exception: 
    #     print('TypeError : Enter a number 2 \n')


# del new_dict['asd']
# print(new_dict['asd'])

# print(sub_divId, ":", new_dict[sub_divId])
# print(type(sub_divId), type(new_dict[sub_divId]))
# print(trees, ":",  sub_divId)
# print(new_dict)

"""Rough work ends"""

''' -- Dict methods and funcs.--
d.get(key, default message)
d.keys()
d.values()
d.items() - both k, v
d.max() - mx key | max(dict, key = d.get) 
d.min() - mn key
d.pop(key, default) - remv k,v pair & return
d.popitem() - remv randm
d.sorted()| sorted(d.keys) | sorted(d.values) 
d.copy() - shallow copy, addrs is copied w/o ref.
'''