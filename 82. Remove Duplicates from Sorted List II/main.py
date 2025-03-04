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
        
        dummy = ListNode(0)  # 建立虛擬頭節點
        dummy.next = head
        prev = dummy
        
        current = head
        while current:
            if current.next and current.val == current.next.val:
                while current.next and current.val == current.next.val:
                    current = current.next
                prev.next = current.next
            else:
                prev = current
            current = current.next
            
        return dummy.next
                    
if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": [1,2,3,3,3,4,4,5], "output": [1, 2, 5]},
        {"input": [1,1,2,3,3], "output": [2]},
    ]
    
    for question in question_list:
        head = ListNode(question['input'][0])
        current = head
        for i in range(1, len(question['input'])):
            current.next = ListNode(question['input'][i])
            current = current.next
            
        output = s.deleteDuplicates(head)
        output.print_list()