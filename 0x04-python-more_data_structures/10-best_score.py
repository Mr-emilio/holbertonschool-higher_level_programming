#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    if a_dictionary:
        return max(zip(a_dictionary.values(), a_dictionaty.keys()))[1]
