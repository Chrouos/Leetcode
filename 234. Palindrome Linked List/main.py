# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head) -> bool:
        
        if head is None: return True
        
        nums = []
        current = head
        half_index = 0
        while current is not None:
            nums.append(current.val)
            current = current.next
            half_index += 0.5
            
        for i in range(int(half_index)):
            if nums[i] != nums[len(nums) - i - 1]: return False
        
        return True
        
if __name__ == '__main__':
    nums = [
        [1],
        [1,1],
        [1, 2, 1],
        [1, 2, 2, 1],
    ]
    
    for num in nums:
        head = ListNode(num[0])
        for i in range(1, len(num)):
            current = head
            while current.next is not None:
                current = current.next
            current.next = ListNode(num[i])
            
        print(Solution().isPalindrome(head))
    