class Stack:
    def __init__(self):
        self.__stack=[]
        self.__top=0

    def push(self,item):
        self.__stack.append(item)
        self.__top+=1

    def pop(self):
        if self.__top>0:
            value=self.__stack[self.__top-1]
            self.__top-=1
            return value
        return "Stack is Empty"
    
    def size(self):
        return self.__top
    
    def isEmpty(self):
        if self.__top<=0:
            return True
        return False


obj=Stack()
obj.push(5)
obj.push(4)
print(obj.isEmpty())
print(obj.pop())
print(obj.size())
print(obj.pop()) 
print(obj.pop()) 
