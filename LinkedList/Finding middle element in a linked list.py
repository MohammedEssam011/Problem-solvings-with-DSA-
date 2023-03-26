# your task is to complete this function

'''
class node:
    def __init__(data):
        self.data = data
        self.next = None
'''
class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def findMid(self, head):
        # Code here
        # return the value stored in the middle node
        count = 0
        mid = head
        curr = head
        
        while curr :
            if count % 2 != 0 :
                mid = mid.next
                
            count  += 1
            curr = curr.next
        
        if mid :
            return mid.data
        
# ----------------------------------------------------------------------------
#using slow fast pointer
# your task is to complete this function

'''
class node:
    def __init__(data):
        self.data = data
        self.next = None
'''
class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def findMid(self, head):
        # Code here
        # return the value stored in the middle node
        fast = head
        slow = head
        while fast and fast.next :
            fast = fast.next.next
            slow = slow.next
            
        return slow.data
