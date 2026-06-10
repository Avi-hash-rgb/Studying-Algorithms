## Node of a Singly linked List
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
    
## Class for defining a Linked List
class LinkedList(object):
    # Initializing the list
    def __init__(self, node = None):
        self.length = 0
        self.head = None

    def printList(self):
        current = self.head # point the current pointer to the first node, the head
        while(current): # till it reaches the end
            print(current.data, end=" -> ") # print the data inline
            current = current.next # point it to the node after the current node
        print("None") # finally print None!
    
    # Getting the length of the Linked List
    # Time Complexity = O(n), for scanning the list of size n
    # Space Complexity = O(1), for creating a temporary variable
    def lengthOfList(self):
        current = self.head # pointing to the first node, the head
        count = 0 # initializing the count to increment it while traversing the list
        while(current != None): # Till current is not None(not at the end), because None points to the end
            count += 1 # increment the count
            current = current.next # move the current pointer forward, so that the count increments
        return count # finally return the count!

    # Singly Linked List insertion
    ## Inserting a new node at the beginning
    def insertAtBeginning(self, data):
        newNode = Node() # initialize a new node to insert
        newNode.data = data # set the data field up

        newNode.next = self.head # point the new Node's next arrow to the current head
        self.head = newNode # shift the head label to point to the brand new Node
        self.length += 1 # increment the length of the list by one

    # Singly Linked List insertion
    ## Inserting a new node at the End
    def insertAtEnd(self, data):
        newNode = Node() # initialize the Node to be at the end
        newNode.data = data # define its data...
        
        if self.head is None:
            self.head = newNode # if the list is empty, the new node becomes the head!
        else:
            current = self.head # point the current pointer towards the first Node, the Head, in order to traverse it to the end
            while(current.next != None): # Till the head reaches the end
                current = current.next  # Point the pointer to the node after that
            current.next = newNode # When it reaches the last node, link it to the new Node
            
        self.length += 1 # increment the length!

    # Singly Linked List insertion
    ## Inserting a new node at a given position
    def insertAtGivenPosition(self, pos, data):
        if pos > self.length or pos < 0: return None # if pos is lesser than 0 or greater than the length, return None
        
        if(pos == 0): # If position = 0, we wanna insert at the start
            self.insertAtBeginning(data)
        elif(pos == self.length): # if pos is length of the list itself, means the last
            self.insertAtEnd(data)
        else:
            newNode = Node() # initialize the new Node
            newNode.data = data # set the data

            count = 0 # initialize the counter to 0 to align perfectly with the target index
            current = self.head # point the current pointer to head of the list, in order to traverse
            while count < pos - 1: # Keep that count running till pos - 1, which is just before when we insert our new Node
                count += 1 # increment the count in order to move forward
                current = current.next # keep moving forward till we reach pos - 1
            
            newNode.next = current.next # Link the node to the rest of the list first
            current.next = newNode # update the current node's next link to your new node
            self.length += 1 # increment the length by one

    # Delete the whole Linked List
    def clear(self):
        self.head = None # if head is set to None, all nodes are automatically cleaned up from memory!
        self.length = 0

    # Delete the head node
    def deleteFromBeginning(self):
        if(self.length == 0): 
            raise ValueError("List cannot be empty")
        
        self.head = self.head.next # point the head to the node after the head to cut off the first node
        self.length -= 1 # decrement the length by 1, because we're deleting

    # Delete the end Node
    def deleteFromEnd(self):
        if(self.length == 0): 
            raise ValueError("List cannot be empty")
        
        if(self.length == 1): # If there's only 1 node, we just empty the head pointer!
            self.head = None
            self.length -= 1
            return

        currentnode = self.head # initialize the current node to the head
        previousnode = self.head # initialize the prev node to the head, both start together
        while(currentnode.next != None): # while the current node reaches the end
            previousnode = currentnode # point the previous node to the current
            currentnode = currentnode.next # move the currentnode pointer forward
        previousnode.next = None # break that arrow pointing to currentnode and replace it with None
        self.length -= 1 # decrement the length by 1, because we're deleting!

    # Delete with Node object from the list
    def deleteFromLinkedListWithNode(self, node):
        if(self.length == 0): raise ValueError("List cannot be empty!")
        
        current = self.head # point current to the first node
        previous = None
        found = False

        while not found:
            if current == node: # if the node object matches our target
                found = True
            elif(current == None): # After traversing if node not found, raise the error
                raise ValueError("Node not in list")
            else:
                previous = current # point prev -> curr
                current = current.next # move curr forward
                
        if previous is None:
            self.head = current.next # if prev is still None, point the head tag to the second node
        else:
            previous.next = current.next # leapfrog move! skips over the target node completely
        self.length -= 1

    # Delete a node at a specific position number
    def deleteAtPosition(self, pos):
        if(pos < 0 or pos >= self.length): # if position is negative or out of bounds, raise error
            raise ValueError("Invalid Position")
        
        if(pos == 0): 
            self.deleteFromBeginning() # if pos is the head, use our ready-made function
        else:
            count = 0
            currentnode = self.head # initialize currentnode to the head
            previousnode = self.head # initialize previousnode to the head
            
            while count < pos: # Loop runs until currentnode lands exactly on the target index
                previousnode = currentnode # point the previous node to currentnode
                currentnode = currentnode.next # move currentnode forward by one
                count += 1 # increment the counter to track our steps
                
            previousnode.next = currentnode.next # leapfrog! previousnode skips completely over currentnode
            self.length -= 1 # decrement the length by 1, because we're deleting!

    # Delete a node containing a specific data value
    def deleteWithValue(self, value):
        if(self.length == 0): 
            raise ValueError("List cannot be empty!") # if the list is completely empty, we can't find anything!
            
        curr = self.head # initialize curr to the first node
        prev = self.head # initialize prev to the first node as well

        # Loop moves forward as long as we haven't hit the end AND haven't found our value
        while(curr.next != None and curr.data != value):
            prev = curr # move prev up to curr
            curr = curr.next # take a step forward with curr
            
        # The loop has stopped. Now let's check if the node we are on actually holds the target value
        if curr.data == value:
            if curr == self.head: 
                self.head = curr.next # if the target value is in the very first node, move the head forward!
            else:
                prev.next = curr.next # leapfrog! prev skips over curr, unhooking the value from the train
            self.length -= 1 # decrement the length by 1, because we're deleting!
            return # we found it and deleted it, so exit the function!
            
        # If the loop finished and we never found the value, raise an error
        raise ValueError("Value not found in list")