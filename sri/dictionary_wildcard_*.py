class Node:
    def __init__(self, value, is_end):
        self.value = value
        # use a hashmap to lookup child nodes in constant time
        # Example: {'a': Node('a'), 'o': Node(o)}
        self.children = {}
        self.is_end = is_end


# Building a trie

def setup(words):
    for word in words:
        add_to_tree(word, root)


def add_to_tree(word, root):
    if word == "":
        root.is_end = True
        return

    next_char, rest_of_string = word[:1], word[1:]
    # If the node already exists in the trie you are building,
    # query it and pass it to the next recursive call
    if next_char in root.children:
        add_to_tree(rest_of_string, root.children[next_char])
        return

    # If the node does not exist, create a new one
    # and add it to its parent
    node = Node(next_char, False)
    root.children[next_char] = node
    # Move on to the next
    add_to_tree(rest_of_string, node)


    #isMember(recursive version)

def isMember(word, node):
    if word == "" and node.is_end:
        return True
    if word == "":
        return False
    next_char, rest_of_string = word[:1], word[1:]
    if next_char == ".":
        for key, child in node.children.items():
            if isMember(rest_of_string, child):
                return True;
    else:
        if next_char in node.children:
            return isMember(rest_of_string, node.children[next_char])

    return False

if __name__ == "__main__":
    root = Node('?',False)
    add_to_tree(root, "hackathon")


# Driver code:
setup(["foo", "bar", "baz"]);
isMember("foo");  # returns true
isMember("garply"); # returns false because "garply" is not in the dictionary
isMember("f.o");  # returns true (it matches foo where the '.' matches the first 'o')
isMember(".."); # returns false (there are no two-letter words)



