"""This script will be exemplative for dict. comprehension"""

liz1 = [11, 2,23 ,34, 2, 3, 43]
# print(liz1)
liz2 = ['as', 'sd', 'wer', 'wr', 'we', 'klj,.', 'oui']
# dict. creation w/o comprehension.
dic = {}
for k, v in zip(liz1, liz2):
    dic[k] = v
  
print(dic)

dic_c = {liz1[i] : liz2[i] for i in range(len(liz1))} # dict. comprehension
print(dic_c)

print([i for i in range(100//3)]) # List comprehension