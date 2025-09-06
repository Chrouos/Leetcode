from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def print_list(self):
        current = self
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return None
        
        current = head
        prev = None
        while current:
            if prev and current.val == prev.val:
                prev.next = current.next
            else:
                prev = current
            current = current.next
            
        return head
    
        
if __name__ == "__main__":
    
    s = Solution()
    question_list = [
        {"input": [1,1,2], "output": [1,2]},
        {"input": [1,1,2,3,3], "output": [1,2,3]},
    ]
    
    for question in question_list:
        head = ListNode(question['input'][0])
        current = head
        for i in range(1, len(question['input'])):
            current.next = ListNode(question['input'][i])
            current = current.next
            
        output = s.deleteDuplicates(head)
        output.print_list()