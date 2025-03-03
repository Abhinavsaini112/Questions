class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class QueueUsingLinkedlist:
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__count=0
        
    def enqueue(self,element):
        newNode=Node(element)
        if self.__head is None:
            self.__head=newNode   
        else:
            self.__tail.next=newNode   
        self.__tail=newNode
        self.__count+=1
        
    def dequeue(self):
        if self.__head is None:
            return "Hey!Queue is Empty"
        data=self.__head.data
        self.__head=self.__head.next
        self.__count-=1
        return data
      
    def isEmpty(self):
        return self.__count==0
           
    def size(self):
        return self.__count
        
    def front(self):
        if self.isEmpty():
            return "Hey! Queue is Empty"
        else:
            return self.__head.data


q=QueueUsingLinkedlist()
q.enqueue(1)
q.enqueue(5)
q.enqueue(3)
q.enqueue(4)
while q.isEmpty() is False:
    print(q.dequeue())
q.front()