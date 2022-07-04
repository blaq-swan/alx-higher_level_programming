#!/usr/bin/python3
"""module for 1-my_list"""


class MyList(list):
    """
    child class of list
    """

    def print_sorted(self):
        """prints sorted self which is a list

        Raises:
            TypeError:
                self must be a list
                self must have integers only
        """

        if not isinstance(self, list):
            raise TypeError("self must be a list")

        for x in self:
            if not isinstance(x, (int)):
                raise TypeError("self must have integers only")

        print(sorted(self))
