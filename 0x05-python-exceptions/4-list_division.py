#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    x = 0
    final_list = []

    while x < list_length:
        y = 0
        try:
            y = my_list_1[x] / my_list_2[x]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            final_list.append(y)
            x += 1
    return final_list
