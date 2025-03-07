from queue import Queue
def reverse_queue(q):
    if q.empty():
        return 
    value=q.get()
    reverse_queue(q)
    q.put(value)


# Queue objects do not support indexing (q[front] will not work)
# You need to convert it to a list before performing index-based operations.
# Incorrect way of passing rear as len(q)
# Queue does not have a len(q), so this will throw an error.
# reverse_queue() does not return anything, and q remains unchanged.
# from queue import Queue
# def reverse_queue(li,rear):
#     front=0
#     while front<rear:
#         li[front],li[rear]=li[rear],li[front]
#         front+=1
#         rear-=1
    
q = Queue()
q.put('a')
q.put('u')
q.put('h')
reverse_queue(q)
while not q.empty():
    print(q.get())