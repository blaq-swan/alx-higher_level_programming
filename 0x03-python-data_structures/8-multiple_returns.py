#!/usr/bin/python3

def multiple_returns(sentence):
    s = sentence
    if s == "":
        return (0, None)
    return (len(s), s[0])
