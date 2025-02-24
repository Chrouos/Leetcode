from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        result = []
        is_carry = 0
        for i in range(len(digits) - 1, -1, -1):
            
            if i == len(digits) - 1:
                result.append((digits[i] + 1) % 10)
                is_carry = (digits[i] + 1) // 10
            else:
                result.append((digits[i] + is_carry) % 10)
                is_carry = (digits[i] + is_carry) // 10
                
        if is_carry == 1:
            result.append(1)
                
        result.reverse()
        return result
        
        
if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": [[1,2,3]], "output": [1,2,4]},
        {"input": [[9,9,9]], "output": [1,0,0,0]},
        {"input": [[8,9,9,9]], "output": [9,0,0,0]},
        {"input": [[1,2,3,9]], "output": [1,2,4,0]},
        {"input": [[0]], "output": [1]},
    ]
    
    for question in question_list:
        print(f"input: {question['input']} => result: {s.plusOne(*question['input'])} == output: {question['output']}")