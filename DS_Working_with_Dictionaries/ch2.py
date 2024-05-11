import csv

with open('TreeOrdersSubset.csv', mode = 'r') as inf:
    orders = list(csv.reader(inf))
    order_counter = {} # Dictionaries can be used as counters, it is one of the most imp apps of dicts.
    # but the counting should not happen from another dict. As dicts. do not by default store redundant items.
    print(len(orders))

    for k, v in orders:
        if k not in order_counter:
            order_counter[k] = int(v)
        else:
            order_counter[k] += int(v)
    print(order_counter.items(),"\n", len(order_counter))

"""Counting dup keys. and adding the values together."""

'''pseudo''' 
# 1. print all the keys to a list using d.get() # ""this is wrong, dictionaries by DEFAULT DON'T ADD REDUNDANT KEYS.""
# 2. loop over the list of keys inside the for the loop, 1st loop is for the list w/ keys, 2nd loop as the keys of dic, if keyItem == k in dict 
# then dict[key] += 1 else: continue
# finally print the new dict w/o dups. check it by adding a key to the dict and running the script again to see the change.

"""Rough Work starts"""
# klist = []
# for key in new_dict.keys(): # 1
#     klist.append(key)
# print(new_dict.keys())

# klist = []
# klist = new_dict.keys()
# print(klist) #1

# klist = []
# for key in new_dict.keys(): # 1, makes the new_dict.keys() object to a list obj. to further looping.
#     klist.append(key)
# print(klist)

"""converting str values of dict to int."""
# print("Dict before type casting: ", new_dict)
# for v in new_dict.values():
#     v = int(v)
# print("\n Dict after type casting: ", new_dict)


# for i in new_dict.keys():
    # for k in new_dict.keys():
# print("Before combining values",new_dict)
# # for i in new_dict.keys(): # Avoids RuntimeError: dictionary changed size during iteration 219
# for k in new_dict.keys(): #1, 2, 3... len(d)
#     if i == k:
#         # new_dict.pop(k) 
#         new_dict[i] = int(new_dict[i])
#         new_dict[k] = int(new_dict[k])
#         new_dict[i] += new_dict[k] # before this we need to cast all values of the dict to int, so that arithmetic ops are possible. 219 = 2
#         # new_dict.pop(k) # Avoids KeyError: key not found.
#     else:
#         pass   
# print("\n\n After combining values",new_dict)
# print("new_length", len(new_dict))

"""psuedo-code for summing up dup key-values"""
# {a:1, b:1, c:1, a:1}
# for i = a:
#     for k = a:
#         a == a: # i == k
#         d.pop(a)
#         new_dict[a] = int('1') + 1 # new_dict[k] = int(new_dict[k]) + 1

#         # at the end i1, d[a] = 1
#         # at the end of i4, d[a] = 2

#         After popping
#         # at the end of i1, d[a] = 1
#         # at the end of i4, d[a] = 2

"""Rough work ends"""