#!/usr/bin/python3
"""module for 1-my_list"""


class MyList(list):
    """
    child class of list
    """
    def print_sorted(self):
        """prints sorted self which is a list"""

        new_list = sorted(self)
        print(new_list)
