class Node:
    def __init__(self,data):
        self.data= data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begin(self,data):
        # Node class ke object ko call kr rha hu 
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    