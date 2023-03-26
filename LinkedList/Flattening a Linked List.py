#User function Template for python3

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        

def merge(a,b):
    if a is None:
        return b
        
    if b is None:
        return a
        
    
    result=None
    
    if a.data<b.data:
        result=a
        result.bottom=merge(a.bottom,b)
    else:
        result=b
        result.bottom=merge(a,b.bottom)
    return result
    
    

def flatten(root):
    if root is None or root.next is None:
        return root
        
    root.next=flatten(root.next)
    root=merge(root,root.next)
    return roo