"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        Time complexity: O(N)
        Memory complexity: O(1) - only fixed additional space used; sentinel(dummy) node gets collected by the GC
        """
        
        q_current = root
        
        while q_current:
            
            q_current_new = Node()
            q_right_new = q_current_new
            
            while q_current:
            
                if x := q_current.left:
                    q_right_new.next = x
                    q_right_new = x
                if x := q_current.right:
                    q_right_new.next = x
                    q_right_new = x
                    
                q_current = q_current.next
            
            q_current = q_current_new.next
        
        return root
