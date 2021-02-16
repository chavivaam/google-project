import re
import glob
import os
from sentence import AutoCompleteData


def clear_str(str_):
    low_str = str_.lower()
    cleared_str =''.join(ch for ch in low_str if ch.isascii() and (ch.isdigit() or ch.isalpha() or ch == ' '))
    clear_space = re.sub(' +', ' ', cleared_str)
    return clear_space


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





