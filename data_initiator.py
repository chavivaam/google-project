import re
import string
import glob
import os
from sentence import AutoCompleteData
import pickle
import sys
import os
import glob
from data_parser import load_data, test_load_data
from data_tree_builder import build_tree


def load_data(data_dict):
    key_counter = 0
    path_base = './Archive'
    flist_files = glob.glob(os.path.join(path_base, '*.txt'))
    for txt_file in flist_files:
       with open(txt_file, 'r', encoding="utf8") as f:
            content = f.read()
            content = content.split('\n')
            for index, row in enumerate(content):
                if row:
                    if len(row) < 200:
                        new_sentence = AutoCompleteData(row, txt_file + ' ' + str(index+1), None, None)
                        data_dict[key_counter] = new_sentence
                        key_counter += 1


def initiate_data():
    test_dict = {}

    # test_load_data(test_dict)
    load_data(test_dict)
    with open('data_dict.obj', 'wb') as fp:
        pickle.dump(test_dict, fp)

    storage_tree = build_tree(test_dict)

    for letter, node in storage_tree.children.items():
        with open('subtrees/sub_tree_' + letter +'.obj', 'wb') as fp:
            pickle.dump(node, fp)


initiate_data()