#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        biggest_int = max(a_dictionary, key=lambda x: a_dictionary[x])
        return (biggest_int)
    return None
