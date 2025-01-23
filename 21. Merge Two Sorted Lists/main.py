from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1
        
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:  
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

def to_linked_list(nums: List[int]) -> Optional[ListNode]:
    if not nums:
        return None
    head = ListNode(nums[0])
    current = head
    for num in nums[1:]:
        current.next = ListNode(num)
        current = current.next
    return head

def to_list(node: Optional[ListNode]) -> List[int]:
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

if __name__ == '__main__':
    loop_list = [
        {"list1": [1, 2, 4], "list2": [1, 3, 4], "result": [1, 1, 2, 3, 4, 4]},
        {"list1": [], "list2": [], "result": []},
        {"list1": [], "list2": [0], "result": [0]},
    ]
    
    sol = Solution()
    for l in loop_list:
        list1 = to_linked_list(l['list1'])
        list2 = to_linked_list(l['list2'])
        expected_result = l['result']
        
        merged_list = sol.mergeTwoLists(list1, list2)
        result = to_list(merged_list)
        
        print(f"Merged List: {result}")
        assert result == expected_result, f"Test failed for input {l}"
        
    print("All tests passed!")
