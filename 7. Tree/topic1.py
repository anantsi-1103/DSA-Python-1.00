# class Node:
    # # constructor 
    # def __init__(self,data):
    #     # only data
    #     self.data = data 
    #     # left part
    #     self.left = None
    #     # right part
    #     self.right = None

from binarytree import Node

root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.left.right= Node(30)
root.left.left= Node(7)

print(root)

# traversal -> inorder , preorder , postorder