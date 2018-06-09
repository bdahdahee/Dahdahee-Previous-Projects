
class Node: #Node class setting up different node commands
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
                          

class Stack: #this class sets up a stack that sets the most recent node to the top of the list
    def __init__(self):
        self.top = None

    def push(self,item):
        newNode = Node(item)
        newNode.next = self.top
        self.top = newNode
     
    def pop(self):
        temp=self.top
        self.top = temp.getNext()
        return temp


def postfix(expression): #This function takes a list with numbers and expression operators returning 
    stack=Stack()   
    expression = expression.split()
    op = "+-/*^"
    for i in expression:
        if i in op:
            num1 = (stack.pop()).getValue()
            num2 = (stack.pop()).getValue()
            if i == "+":
                num = num1 + num2
                stack.push(num)
            if i == "-":
                num = num2 - num1
                stack.push(num)
            if i == "/":
                num = num2 / num1
                stack.push(num)
            if i == "*":
                num = num1 * num2
                stack.push(num)
            if i == "^":
                num = num2 ** num1
                stack.push(num)
        else:
            i = float(i)
            stack.push(i)
    val = (stack.pop()).getValue()
    if val % 1 == 0:
        val = int(val)
        stack.push(val)
    else:
        stack.push(val)

    return stack.pop()   
