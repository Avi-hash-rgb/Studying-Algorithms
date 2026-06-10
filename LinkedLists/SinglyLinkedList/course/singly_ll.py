class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value, end = " ")
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return 
        
        curr = self.head
        prev = self.head
        while(curr.next):
            prev = curr
            curr = curr.next
            
        self.tail = prev
        self.tail.next = None

        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return curr

    def pop_first(self):
        if(self.length == 0):
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if(self.length == 0):
            self.tail = None
        return temp
    
    def get(self, index):
        if(index < 0 or index >= self.length):
            return None

        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.value
    
    def set_value(self, index, value):
        if(index < 0 or index >= self.length):
            return None
        
        curr = self.head
        for _ in range(index):
            curr = curr.next
        if curr:
            curr.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index > 0 or index < self.length:
            return False
        if index == 0: 
            return self.pop_first()
        if index == self.length: 
            return self.pop()

        curr = self.head
        while(curr and curr.next):
            if(curr.value == temp):
                curr.next = curr.next.next
            curr = curr.next
        self.length -= 1
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(5)

my_linked_list.prepend(3)
my_linked_list.prepend(4)

my_linked_list.pop()
my_linked_list.pop_first()

my_linked_list.insert(2, 5)

my_linked_list.print_list()