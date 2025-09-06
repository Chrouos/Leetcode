from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        '''
        給定兩個非空的鏈表 l1 和 l2，表示兩個非負整數。這些數字是以逆序方式存儲的，每個節點包含一位數。
        '''
        
        Node = ListNode
        
        dummy = Node(0)
        current = dummy
        p, q = l1, l2 
        carry = 0
        
        while p or q :
            total = carry + (p.val if p else 0) + (q.val if q else 0)
            carry, digit = divmod(total, 10)
            
            current.next = Node(digit)
            current = current.next
            
            if p: p = p.next
            if q: q = q.next
        
        if carry > 0:
            current.next = Node(carry)
        
        return dummy.next
            
            
            
        
        

if __name__ == "__main__":
    s = Solution()
    
    question_list = [
        {"input": ([2, 4, 3], [5, 6, 4]), "output": [7, 0, 8]},  # 342 + 465 = 807
        {"input": ([0], [0]), "output": [0]},                    # 0 + 0 = 0
    ]
    
    for question in question_list:
        l1_values, l2_values = question["input"]
        expected_output = question["output"]
        
        # Build linked lists from input values
        l1 = ListNode(l1_values[0])
        current = l1
        for value in l1_values[1:]:
            current.next = ListNode(value)
            current = current.next
        
        l2 = ListNode(l2_values[0])
        current = l2
        for value in l2_values[1:]:
            current.next = ListNode(value)
            current = current.next
        
        # Call the method and get the result
        result = s.addTwoNumbers(l1, l2)
        
        # Convert result linked list to a list for comparison
        result_values = []
        while result:
            result_values.append(result.val)
            result = result.next
        
        print(f"[{result_values == expected_output}] input: {question['input']}, output: {result_values}, expected_output: {expected_output}")