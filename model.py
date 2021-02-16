import pickle
import glob
import os
from tree import Node


class DataModel:
    def __init__(self):
        self.base_data = None
        self.completions_tree = Node([])

        with open('data_dict.obj', 'rb') as f:
            self.base_data = pickle.load(f)

        root_children = {}
        path_base = 'subtrees'
        flist_files = glob.glob(os.path.join(path_base, '*.obj'))
        for obj_file in flist_files:
            with open(obj_file, 'rb') as f:
                file_prefix = obj_file.split('.')
                letter = file_prefix[0][-1]
                new_node = pickle.load(f)
                root_children[letter] = new_node

        self.completions_tree.children = root_children

    def get_base_data(self):
        return self.base_data

    def get_completions_tree(self):
        return self.completions_tree

    # @staticmethod
    # def get_root_child(letter):
    #     try:
    #         file_name = 'subtrees/sub_tree_' + letter + '.obj'
    #         with open(file_name, 'rb') as f:
    #             new_node = pickle.load(f)
    #         return new_node
    #     except Exception as e:
    #         raise FileNotFoundError()





