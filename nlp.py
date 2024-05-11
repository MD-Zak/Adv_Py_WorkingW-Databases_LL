"""This program is used to test the amount of time taken by functions that call other functions."""

import re

def stem(word):
    """Return the stem of a word

    >>> stem(working)
    'work'
    >>> stem(speeds)
    'speed' 
    """
    return re.sub(r'(s|ing)$','',word)


def tokenize(text):
    """Split text to words , ignoring stop words"""
    tokens = []
    for ele in re.findall('[a-zA-Z]+', text):
        ele = ele.lower()
        ele = stem(ele)
        if ele not in stop_words:
            tokens.append(ele)
    return tokens

stop_words = ['we', 'will', 'to', 'the', 'a', 'is', 'in', 'you', 'and']

