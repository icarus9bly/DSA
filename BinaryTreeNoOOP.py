from pprint import pprint


def bt(root):
    return [root, [], []]


# Adding to left side of tree


def insert_left(root, new_branch):
    elem = root.pop(1)
    if len(elem) > 1:
        root.insert(1, [new_branch, elem, []])  # append new branch
    else:
        root.insert(1, new_branch)
    return root


def insert_right(root, new_branch):
    elem = root.pop(2)
    if len(elem) > 1:
        root.insert(2, [new_branch, [], elem])
    else:
        root.insert(2, new_branch)


tree = bt(3)
insert_left(tree, [76, 88, 89])
insert_right(tree, 99)
print(tree)
