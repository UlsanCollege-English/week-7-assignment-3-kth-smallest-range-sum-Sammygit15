class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    """
    Insert key into BST, rejecting duplicates.
    Returns the (possibly new) root.
    """
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    # If key == root.key, duplicate: do nothing
    return root
def kth_smallest(root, k):
    """
    Return the 1-based kth smallest key in BST.
    Raises IndexError if k is larger than the number of nodes.
    """
    count = 0
    result = None

    def inorder(node):
        nonlocal count, result
        if node is None or result is not None:
            return
        inorder(node.left)
        count += 1
        if count == k:
            result = node.key
            return
        inorder(node.right)

    inorder(root)
    if result is None:
        raise IndexError("k is larger than the number of nodes in BST")
    return result


def range_sum_bst(root, low, high):
    """
    Return the sum of all keys in the inclusive range [low, high].
    Prune subtrees that cannot contain valid keys.
    """
    if root is None:
        return 0

    total = 0
    if root.key >= low:
        total += range_sum_bst(root.left, low, high)
    if low <= root.key <= high:
        total += root.key
    if root.key <= high:
        total += range_sum_bst(root.right, low, high)
    return total
