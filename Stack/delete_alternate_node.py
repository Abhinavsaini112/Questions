class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def deleteAlternateNodes(head):
    # Write your code here
    if head is None:
        return None
    current =head
    while current  and current.next :        
        current.next=current.next.next
        current=current.next
    return head

