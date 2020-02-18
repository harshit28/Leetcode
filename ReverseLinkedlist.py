# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        temp = head
        s=[]
        while temp:
            s.append(temp.val)
            temp = temp.next
        return s[:]==s[::-1]    
                
        