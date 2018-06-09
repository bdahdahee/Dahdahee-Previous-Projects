
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
                          
class LinkedList: # creates a new list that is empty
    def __init__(self):
        self.head=None
        self.tail=None

    def insert(self, after, item): #adds a new Node with value=item to the list after the Node with value=after
        n1 = Node(item)
        if self.head is None and self.tail is None:
          n1.next = None
          self.head = n1
          self.tail = self.head
          return
        elif (after == self.head.value and self.head.value != self.tail.value):
          n1.next = self.head
          self.head = n1
          return
        else:
          l1 = self.head
          while (l1.value != after) :
            l1 = l1.next
          n1.next = l1.next
          l1.next = n1
          return

    def pop(self): # removes and returns the value of the last Node in the list
        temp=self.head
        self.tail = None
        while temp:
            if temp.next.next == None:
              self.tail = temp
              poppedvar = temp.next
              temp.next = None
              return poppedvar
            else:
              temp=temp.next
    

    def append(self, value): #adds a new Node with value=item to the end of the list
        if self.head==None:
            new_node=Node(value)
            self.head=new_node
            self.tail=self.head
        elif self.tail==self.head:
            self.tail=Node(value)
            self.head.setNext(self.tail)
        else:
            new_node=Node(value)
            self.tail.setNext(new_node)
            self.tail=new_node



    def remove(self, value): #removes the Node with value=item from the list. It needs the item and modifies the list
        current=self.head
        previous=None
        found=False
        while not found:
            if current.getValue()==value:
                found=True
            else:
                previous=current
                current=current.getNext()

        if previous==None:
            self.head=current.getNext()
        elif current.getNext()==None:
            self.tail=previous
            previous.setNext(None)
        else:
            previous.setNext(current.getNext()) 




    def isEmpty(self): #tests if the list is empty
        return self.head == None


    def add(self, value): #adds a new item to the beginning of the list
        new_node=Node(value)
        new_node.setNext(self.head)
        self.head=new_node

        if self.size()==1:
            self.tail=new_node


    def search(self,value): #searches for the Node using the given value
        current=self.head
        found=False
        while current!=None and not found:
            if current.getValue()==value:
                return True
            else:
                current=current.getNext()
        return found


    def printList(self):
        temp=self.head
        while temp:
            print(temp.value, end=' ')
            temp=temp.next

