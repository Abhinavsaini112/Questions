class Queue:
    def __init__(self):
        self.__s1,self.__s2=[],[]
        self.__count=0

    def enqueue(self,data):
        while len(self.__s1)!=0:
            self.__s2.append(self.__s1.pop())
        self.__s1.append(data)
        while len(self.__s2) !=0:
            self.__s1.append(self.__s2.pop())
        self.__count+=1
    
    def dequeue(self):
        if self.__count==0:
            return "Empty Queue"
        ele =self.__s1.pop()
        self.__count-=1
        return ele
    
    def front(self):
        if self.__count==0:
            return 'Empty Queue'
        return self.__s1[-1]
    
    def size(self):
        return self.__count
    
    def isEmpty(self):
        return self.size()==0
    
    

q=Queue()
q.enqueue('a')
q.enqueue('b')
q.enqueue('d')
q.enqueue('g')
print(q.size())
print(q.isEmpty())
print(q.front())
while not q.isEmpty() :
    print(q.dequeue())

