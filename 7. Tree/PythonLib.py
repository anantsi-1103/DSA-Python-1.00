# pip install binarytree

from binarytree import Node, bst

root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.left.left = Node(2)
root.left.right = Node(7)


# print("Binary Tree Structure")
# print(root)

# traversal

print("inorder : ", root.inorder)
print("preorder : ", root.preorder)
print("postorder : ", root.poster)


root.height
root.size