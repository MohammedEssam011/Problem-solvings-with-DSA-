class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# your task is to complete this function
# function should return true/false or 1/0
def isCircular(head):
    # Code here
    if not head :
        return False
        
    curr = head.next
    while((curr) and (curr != head)):
        curr = curr.next
    return curr == head
        