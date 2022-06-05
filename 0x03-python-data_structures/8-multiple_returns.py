#!/usr/bin/python3

def multiple_returns(sentence):
    string = [x for x in sentence]
    if len(string) == 0:
        string[0] = None
    else:
        return (len(string), string[0])
