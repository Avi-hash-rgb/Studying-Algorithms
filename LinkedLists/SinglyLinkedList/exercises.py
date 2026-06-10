class Node:
    # Constructor
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    
    # Method for setting the data field of the Node
    def setData(self, data):
        self.data = data
    
    # Method for getting the data field of the Node
    def getData(self):
        return self.data
    
    # Method for setting next field of the Node
    def setNext(self, next):
        self.next = next

    # Method for getting next field of the Node
    def getNext(self):
        return self.next
    
    # Returns true if the node points to another node
    def hasNext(self):
        return self.next != None
    
class LinkedList(object):
    def __init__(self, node=None):
        self.head = None
        self.length = 0
    # 1. print the length of the linked list
    def printLength(self):
        curr = self.head
        count = 0
        while(curr != None):
            curr = curr.next
            count += 1
        
        return count
    
    # 2. search an element in the linked list
    def isPresent(self, element):
        curr = self.head
        found = False

        while(curr != None):
            if(curr.data == element):
                found = True
            curr = curr.next
        return found
    
    # 3. Print the linked list
    def printLinkedList(self):
        curr = self.head
        while(curr != None):
            print(curr.data, "->")
            curr = curr.next
        return None
    
    # 4. Insert at the head of a Linked list
    def insertAtBeginning(self, data):
        newNode = Node()
        newNode.data = data
        
        newNode.next = self.head
        self.head = newNode
        self.length += 1

    # 5. Insert At the End
    def insertAtEnd(self, data):
        newNode = Node()
        newNode.data = data

        curr = self.head
        if(self.length == 0):
            self.head = newNode

        while(curr != None):
            curr = curr.next
        curr.next = newNode
        self.length += 1

    # 6. Get the tail Node
    def getLastNode(self):
        curr = self.head
        while(curr != None):
            curr = curr.next
        return curr
    
    # 7. Get head Node
    def getheadNode(self):
        return self.head
    