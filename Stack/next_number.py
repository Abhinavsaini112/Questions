## Read input as specified in the question.
## Print output as specified in the question.
# Problem ID 328 Midpoint LL
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def nextNumber(head):
    #Implement Your Code here
    stack=[]
    while head is not None:
        stack.append(head.data)
        head=head.next
    carry=1
    while stack:
        digit=stack.pop()
        total=digit+carry
        x=total%10
        newnode=Node(x)
        newnode.next=head
        head=newnode
        carry=total//10
    if carry:
        new_node = Node(carry)
        new_node.next = head
        head = new_node        
    return head
        
def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def printll(head):
    while head is not None:
        print(head.data,end= ' ')
        head = head.next
    return

# Main
# Read the link list elements including -1
arr=[int(ele) for ele in input().split()]
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
head = nextNumber(l)
printll(head)