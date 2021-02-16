from tree import Node
from data_parser import clear_str


def build_subtree(letter, index, sentence, sentence_id, root):
    offset = index
    root.add_child(sentence_id, offset, letter)
    last_added = root.children[letter]
    index += 1
    max_depth = 1
    while index < len(sentence) and max_depth <= 15:
        letter = sentence[index]
        last_added.add_child(sentence_id, offset, letter)
        last_added = last_added.children[letter]
        index += 1
        max_depth += 1


def build_tree(sentences):
    root = Node([])
    for s_id, str_object in sentences.items():
        if s_id < 50000:
            if s_id % 1000 == 0:
                print(s_id)
            cleared_str = clear_str(str_object.completed_sentence)
            word_start = True
            for index, letter in enumerate(cleared_str):
                if word_start:
                    build_subtree(letter, index, cleared_str, s_id, root)
                    word_start = False
                if letter == ' ':
                    word_start = True

    return root
