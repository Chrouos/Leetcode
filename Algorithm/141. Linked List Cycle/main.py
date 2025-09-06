from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
    def print_list(self):
        current = self
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        '''
        判斷鏈表是否有環
        解法：
        使用快慢指針，如果有環，快指針和慢指針會相遇。
        '''
        if not head: return False

        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: return True
            
        return False


def build_linked_list_with_cycle(values, pos):
    """
    values: 節點的數值列表
    pos: 尾節點連回的索引（-1 表示無環）
    """
    if not values:
        return None
    
    nodes = [ListNode(v) for v in values]
    
    for i in range(len(values) - 1):
        nodes[i].next = nodes[i + 1]
    
    if pos != -1:
        nodes[-1].next = nodes[pos]  # 尾節點指向 pos 節點，形成環
    
    return nodes[0]

if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": ([3, 2, 0, -4], 1), "output": True},   # 有環，尾節點連回 index=1 (值=2)
        {"input": ([1, 2], 0), "output": True},          # 有環，尾節點連回 index=0 (值=1)
        {"input": ([1], -1), "output": False},           # 無環
    ]
    
    for question in question_list:
        values, pos = question["input"]
        expected_output = question["output"]
        
        head = build_linked_list_with_cycle(values, pos)
        
        result = s.hasCycle(head)
        print(f"[{result == expected_output}] input: {values}, pos={pos}, output: {result}, expected_output: {expected_output}")
