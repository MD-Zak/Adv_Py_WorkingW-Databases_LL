# import re

# txt = "hello how are you doing?"\
# "this is a practice to find the numbers of 'a"\
# "a module is going to be used to a"

"ex1"
# x = re.search("hello", txt)
# if x:
#     print(1) # prints 1 as pattern will be found in the text with the word.
# else:
#     print(0)

"ex2"
# x = re.findall('re', txt) #finds all occurences, even within a word; with same order of the pattern.
# print(len(x)) # should print 1

"ex3"
# l = [5, 10, 7, 11, 323, 23]
# l[2] =3
# l[3] = 23
# l[4] = 3
# print(l)
# l = tuple(l) #tuple obj's are immutable
# l[0] = 12
# l[4] = 90
# print(l)

"ex4"

# class sampleexception(Exception):
#     pass
# class Account:
#     acc_lyst = [1001, 1004, 1005, 1009]
#     def validate_acc(self, acc_id):
#         stats = 0
#         for id in self.acc_lyst:
#             if(acc_id == id):
#                 stats = 1
#                 break
#         # if(stats!=0): # This is required for the loop's next iteration.
#         #     return "hello"
#         else:
#             raise sampleexception #can create any exception name required, just have to base the class on the Exception class.
#                 # here sampleexception is raised as an Exception, serving the purpose as intended.
# try:
#     acc1 = Account()
#     acc1.validate_acc(10012)
#     print("acc valid")
# except sampleexception: # the except clause expects sampleexception.
#     print("invalid num")

"ex5"

# # def control():
# #     print('The control has been switched')
# def calc(n1, n2, op):

#     if (op == "+"):
#         return n1 + n2
#     elif(op == "-"):
#         return n1 - n2
#     elif(op == "*"):
#         return n1 * n2
#     elif(op == "/"):
#         return n1 / n2
#     else:
#         return "Invalid operator"
# try:
#     num1 = float(input('Enter a number: '))
#     num2 = float(input('Enter another number: '))
#     op = input('Enter any one of the operation (+,-,*,/): ')
#     result = calc(num1,num2, op)
#     print(result)
# except ValueError:
#     print('Invalid input, enter valid numbers.')
#     # control() # this way you can use the try-catch block to continue execution, after catching the error.
# except ZeroDivisionError:
#     print('Division by zero, not allowed.')
    
"ex6"

# def func(n):
#     return n * n
 
# num = (1,2,3, 4)
# r = map(func, num) # applies the func. func to all the numbers in the iterable num, returns an map object, that is also iterable.
# num = map(func, num) # Storing to tuple, also does not create an err.
# print(sum(list(r)))
# print(sum(num)) # also works w/o casting to list
# print(type(r), type(num)) 

"ex7"

# "Can tuples have dups?"
# t = (1, 23, 4,4, 5, 43) # tuples can have duplicates.
# l = [1, 23, 4,4, 5, 43] # just like lists.
# print(t, l)
# "Can tuples be added to tuples?" 
# t = t + (1, 2, 4, 3, 2) # tuples can be added to other tuples.
# print(t)
# # t = t + l # TypeError: can only concatenate tuple (not "list") to tuple
# print(t)
# "How does dict retains Values for duplicate keys?"
# d = {1:3, 1:4, 2:3, 3: 4, 2:6} # dict. retains the highest values for each key. -- false, check below.
# print(d) # d = {1: 4, 2: 6, 3: 4}
# d = {1:2, 1: 'asd', 1: 4, 2:3, 2:'asdf', 2:5} # There is no priority of ints over str during retention.
# print(d) # d = {1: 4, 2: 5}
# d = {1:4, 'one': 2, "one":'last_value', 1:'qwe', 1:2, 2:'twoer', 'two':2, "two": "two", 2: "wow", "two": "pow", "two": 1}
# print(d) # d = {1: 4, 'one': 1, 2: 3, 'two': 'wow'} and after change {1: 4, 'one': 1, 2: 'wow', 'two': 'wow'}
# # The dict only retains the MOST RECENT ENTRY. As most recent entry over writes the previous k-v pair association.
# "Can dicts be added to tuples, we know lists cannot be?"
# # t = t + d
# print(t) # TypeError: can only concatenate tuple (not "dict") to tuple
# "Can tuples' elements be indexed and assigned, aka changed?"
# # t[2] = 9 # TypeError: 'tuple' object does not support item assignment
# print(t[2]) # They can be indexed, but not assigned. As tuples are immutable objs.
# "Can tuples concatenate strs?"
# st = "hello"
# t = t + st
# print(t) # TypeError: can only concatenate tuple (not "str") to tuple

"ex8"

# A = ['XZ', 'TV', 'ABCD', '123']
# print(list(map(list, A))) # [['X', 'Z'], ['T', 'V'], ['A', 'B', 'C', 'D'], ['1', '2', '3']]
# print(list(map(str, A))) # ['XZ', 'TV', 'ABCD', '123'] # str func, iterated through each ele and returned the same as they are already strs.
# # print(list(map(int, A))) # ValueError: invalid literal for int() with base 10: 'XZ'
# B = [12, 33, 323, 454, 3456]
# print(list(map(int, B)))
# "Syntax of map(func, iterable1, iterable2, ...) returns an iterable map obj"

# st  = 'Hello' # "str objs are iterable."
# print(list(st)) # ['H', 'e', 'l', 'l', 'o'] 

# # Thus, when list was used as an func to map, it took the iterable list A, and applied the list function of making objs to list to each ele.
# # This is why each ele, is returned with its own list.

# n = 112211
# # n = 1122a11 # SyntaxError: invalid decimal literal
# # print(list(n)) # TypeError: 'int' object is not iterable
# print(str(n)) # 112211
# print(list(str(n))) # ['1', '1', '2', '2', '1', '1'], "str objs are iterable."