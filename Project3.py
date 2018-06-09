
class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    def setValue(self,new_value):
        self.value = new_value

    def setNext(self,new_next):
        self.next = new_next

    def __str__(self):
        return ("{}".format(self.value)) 

    __repr__ = __str__


class Queue: # creates a new queue that is empty. It needs no parameters and returns nothing 

    def __init__(self):
        self.count = 0
        self.head = None
        self.tail = None
    
    def isEmpty(self): # tests to see whether the queue is empty
        count = self.count
        if count == 0:
            return True
        else:
            return False
   
    def size(self): #returns the number of items in the queue
        count = self.count
        return count    

    def enqueue(self, item): # adds a new Node with value=item to the tail of the queue
        if self.head is None and self.tail is None:
            newNode = Node(item)
            self.head = newNode
            self.tail = self.head
            self.count += 1
        else:
            newNode = Node(item)
            self.tail.next = newNode
            self.tail = newNode
            newNode.previous= self.tail
            self.count +=1
    def dequeue (self): # removes the head Node from the queue. It needs no parameters and returns the value of the Node removed from the queue
            count = self.count
            if count > 1: 
                temp = self.head
                self.head = self.head.next
                self.count -= 1
                return temp
            if count == 1:
                temp = self.head
                self.head= None
                self.tail= None
                self.count -= 1
                return temp 
            if count == 0:
                return "Queue is empty"

      
    def printQueue(self):
        temp = self.head
        while (temp):
            print(temp.value, end=' ')  
            temp = temp.next

