#!/usr/bin/python3
def no_c(my_string):
    new_list = list(my_string)
    for x in new_list:
        if x == 'c':
            new_list.remove('c')
        if x == 'C':
            new_list.remove('C')
    my_string = "".join(new_list)
    return my_string
