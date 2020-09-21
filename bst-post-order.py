# Python program to for tree traversals

# A class that represents an individual node in a
# Binary Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    # A function to do inorder tree traversal


def printInorder(root):
    if root:
        # First recur on left child
        printInorder(root.left)

        # then print the data of node
        print(root.val),

        # now recur on right child
        printInorder(root.right)

    # A function to do postorder tree traversal


def printPostorder(root):
    if root:
        # First recur on left child
        printPostorder(root.left)

        # the recur on right child
        printPostorder(root.right)

        # now print the data of node
        print(root.val),

    # A function to do preorder tree traversal


def printPreorder(root):
    if root:
        # First print the data of node
        print(root.val),

        # Then recur on left child
        printPreorder(root.left)

        # Finally recur on right child
        printPreorder(root.right)

    # Driver code


root = Node('+')
root.left = Node(3)
root.right = Node('*')
root.left.left = Node('-')
root.right.right = Node('+')
root.right.left = Node(4)
root.right.left.right = Node('*')
root.right.right.left = Node(3)
root.right.right.right = Node('-')
root.right.left.right.left = Node(7)
root.right.left.right.right = Node(9)
root.right.right.right.left = Node(6)
root.right.right.right.right = Node(2)

# Example: Postorder traversal for the above given figure is 4 5 2 3

"""
(a) Inorder (Left, Root, Right) : 4 2 5 1 3
(b) Preorder (Root, Left, Right) : 1 2 4 5 3
(c) Postorder (Left, Right, Root) : 4 5 2 3 1

Breadth First or Level Order Traversal : 1 2 3 4 5
"""

print("Preorder traversal of binary tree is:")
# printPreorder(root)


print("\nInorder traversal of binary tree is")
printInorder(root)


print("\nPostorder traversal of binary tree is")
# printPostorder(root)