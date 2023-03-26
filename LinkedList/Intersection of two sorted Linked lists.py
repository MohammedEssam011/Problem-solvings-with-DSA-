#User function Template for python3


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
        
def findIntersection(head1,head2):
    p1 = head1
    p2 = head2
    head = None
    tail = None
    
    while p1 and p2:
        if p1.data > p2.data:
            # nodes dont match
            # moving to next node in list with smaller node
            p2 = p2.next
        
        elif p2.data > p1.data:
            # nodes dont match
            # moving to next node in list with smaller node
            p1 = p1.next
        
        else:
            # if nodes match:
            
            if head is None:
                head = tail = Node(p1.data)
                # creating new head for intersection list
            else:
                tail.next = Node(p1.data)
                tail = tail.next
                # appending new node at the end
            
            p1=p1.next
            p2=p2.next
            # moving to next nodes in both lists
    
    return head






