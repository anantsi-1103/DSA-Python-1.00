class Node:
    # constructor 
    def __init__(self,data):
        # only data
        self.data = data 
        # left part
        self.left = None
        # right part
        self.right = None


# root = Node("A")
# root.left = Node("B")
# root.right = Node("C")
# root.left.right= Node("D")
# root.right.left= Node("E")
# root.right.right= Node("F")
# root.right.left.left= Node("G")
# root.right.right.left= Node("H")
# root.right.right.right= Node("I")



# print(root)

# traversal -> inorder , preorder , postorder

# def inorder(root):
#     if root: 
#         inorder(root.left) #left
#         print(root.data,end=" ") #root
#         inorder(root.right) #right


# def preorder(root):
#     if root: 
#         print(root.data,end=" ") #root
#         preorder(root.left) #left
#         preorder(root.right) #right

# def postorder(root):
#     if root: 
#         postorder(root.left) #left
#         postorder(root.right) #right
#         print(root.data,end=" ") #root
   

# inorder(root)

def insert(root,value):
    if root is None:
        return Node(value)
    
    if value < root.data:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def search(root,key):
    if root is None:
        return False
    
    if root.data == key:
        return True

    if key < root.data:
        return search(root.left , key)
    
    else:
         return search(root.right , key)

def height(root):
    if root is None:
        return -1
    
    return 1 + max((height(root.left)),(height(root.right)))


def count(root):
    if root is None:
        return 0
    
    return 1 + count(root.left) + count(root.right)



root = None
val = [10,4,3,5,7,20,25]

for v in val:
    root = insert(root, v)




print(search(root, 70))

print(height(root))

print(count(root))