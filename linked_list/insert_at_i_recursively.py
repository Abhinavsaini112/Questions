class node:
    def __init__(self,data):
        self.data=data
        self.next=None
def takeinput():
    inputlist=[int(ele) for ele in input().split()]
    head=None
    for currData in inputlist:
        if currData==-1:
            break
        newNode=node(currData)
        if head is None:
            head=newNode
        else:
            curr=head
            while curr.next is not None:
                curr=curr.next
            curr.next=newNode
    return head
def length(head):
    count=0
    while head is not None:
        count=count+1
        head=head.next
    return count
def printLL(head):
    while head is not None:
        print(str(head.data)+'->',end='')
        head=head.next
    return


def insert_at_i_recursively(head,i,data):
    if i<0 :
        return head
    if i==0:
        new_node=node(data)
        new_node.next=head
        return new_node
    if head is None:
        return 
    small_head=insert_at_i_recursively(head.next,i-1,data)
    head.next=small_head
    return head


head = takeinput()
print("Original Linked List: ")
printLL(head)
print()
# Insert new node recursively at index 1
new_head = insert_at_i_recursively(head, 1, 85)
print("Linked List after insertion at index 1: ")
printLL(new_head)