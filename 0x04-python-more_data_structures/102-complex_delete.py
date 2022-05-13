#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keyss = list(a_dictionary.keys())
    valuess = list(a_dictionary.values())
    for i, key in enumerate(keyss):
        if value is valuess[i]:
            del a_dictionary[key]
    return a_dictionary
