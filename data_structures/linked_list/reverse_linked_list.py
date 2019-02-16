class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

def reverse_linked_list(node):
    if node is None or node.next is None:
        return node

    rev, curr = node, node.next
    rev.next = None

    while curr:
        store = curr.next
        curr.next = rev
        rev = curr
        curr = store

    return rev
