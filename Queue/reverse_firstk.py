from queue import Queue
def reverse_firstk_elements(q,k):
    if q.empty() or k>q.qsize():
        return 
    if k<=0:
        return
    stack1=[]
    stack2=[]
    for i in range(k):
        stack1.append(q.get())
    while not q.empty():
        stack2.append(q.get())
    for i in range(k):
        q.put(stack1.pop())
    for j in stack2:
        q.put(j)
    return q

q = Queue()
q.put(42)
q.put(24)
q.put(32)
q.put(45)
q.put(88)
reverse_firstk_elements(q,4)    
while not q.empty():
    print(q.get(), end=" ")