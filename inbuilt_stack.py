from queue import LifoQueue
import random

stack=LifoQueue(maxsize=15)
print(stack.maxsize)

number=[random.randint(1,100) for _ in range(10)]
print(number)
for i in number:
    stack.put(i)

print('Size of the stack',stack.qsize())

for j in range(5):
    print(stack.get())

print(stack.full())