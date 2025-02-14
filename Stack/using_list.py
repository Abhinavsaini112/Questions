class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.head=None
        self.count=0

    def push(self,data):
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode
        self.count+=1

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        value=self.head.data
        self.head=self.head.next
        self.count-=1
        return value
     
    def top(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.head.data
    
    def size(self):
        return self.count
    
    def isEmpty(self):
        if self.count==0:
            return True
        return False
    
obj=Stack()
obj.push(5)
obj.push(4)
print(obj.isEmpty())
print(obj.pop())
print(obj.top())
print(obj.size())
print(obj.pop()) 
print(obj.pop()) 
    