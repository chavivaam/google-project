class Node:
    def __init__(self, data):
        self.children = {}#{(letter: Node), (letter2, Node2)}
        self.data = data#[(id1, offset1), (id2, offset2)..]

    def add_child(self, sentence_id, offset, letter):
        if letter in self.children.keys():
            ids = [item[0] for item in self.children[letter].data]
            if sentence_id not in ids:
                self.children[letter].data.append((sentence_id, offset))
        else:
            new_node = Node([(sentence_id, offset)])
            self.children[letter] = new_node
