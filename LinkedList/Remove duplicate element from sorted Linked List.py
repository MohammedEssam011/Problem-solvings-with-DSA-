#User function Template for python3
'''
	Your task is to remove duplicates from given 
	sorted linked list.
	
	Function Arguments: head (head of the given linked list) 
	Return Type: none, just remove the duplicates from the list.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
#Function to remove duplicates from sorted linked list.
#Function to remove duplicates from sorted linked list.
def removeDuplicates(head):
    
    #using a pointer to iterate over linked list.
    curr_node=head
    
    #traversing through the linked list.
    while curr_node.next:
        
        #if data at current node and next node are same, we store the node 
        #next to the next node of current node in link of current node.
        if(curr_node.data == curr_node.next.data):
            curr_node.next = curr_node.next.next
            
        #else we just move the pointer to next node.
        else:
            curr_node=curr_node.next