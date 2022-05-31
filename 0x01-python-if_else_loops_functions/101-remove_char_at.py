#!/usr/bin/python3

def remove_char_at(str, n):
    string_list = [x for x in str]

    for x in string_list:
        if string_list.index(x) == n:
            string_list[n] = ''
    return ''.join(string_list)
