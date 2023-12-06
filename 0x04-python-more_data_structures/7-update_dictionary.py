#!/usr/bin/python
def update_dictionary(a_dictionary, key, value):
    n_dic = {key: value}
    a_dictionary.update(n_dic)
    return a_dictionary
