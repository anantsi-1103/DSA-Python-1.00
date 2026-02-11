class Node:
    # constructor 
    def __init__(self,data):
        # only data
        self.data = data 
        # left part
        self.left = None
        # right part
        self.right = None


root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.left.right= Node(30)
root.left.left= Node(7)



# print(root)

# traversal -> inorder , preorder , postorder

def inorder(root):
    if root: 
        inorder(root.left) #left
        print(root.data,end=" ") #root
        inorder(root.right) #right


def preorder(root):
    if root: 
        print(root.data,end=" ") #root
        preorder(root.left) #left
        preorder(root.right) #right

def postorder(root):
    if root: 
        postorder(root.left) #left
        postorder(root.right) #right
        print(root.data,end=" ") #root
   


preorder(root)