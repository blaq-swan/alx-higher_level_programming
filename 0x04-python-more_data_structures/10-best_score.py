#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    keys, values = list(a_dictionary.keys()), list(a_dictionary.values())
    score = sorted(list(zip(keys, values)), key=lambda x: x[1], reverse=True)

    return score[0][0]
