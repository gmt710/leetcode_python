# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        q = []
        while(head):
            q.append(head.val)
            head = head.next
        
        if q == q[::-1]:
            return True  
        else:
            return False
        
