# https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/?envType=daily-question&envId=2025-03-19
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        if sum(nums) == len(nums): return 0
        
        nums_copy = nums.copy()
        count = 0
        for i in range(len(nums_copy)):
            if nums_copy[i] == 0 and i + 2 < len(nums_copy):
                for j in range(i,  i + 3):
                    nums_copy[j] ^= 1
                count += 1
                    
        if count != 0 and sum(nums_copy) == len(nums_copy):
            return count  
        else: return -1
        
if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": [[0,1,1,1,0,0]], "output": 3},
        {"input": [[0,1,1,1]], "output": -1},
        {"input": [[0,0,0]], "output": 1},
    ]
    
    for question in question_list:
        output = s.minOperations(*question['input'])
        print(f"[{output == question['output']}] input: {question['input']}, output: {output}, expected: {question['output']}")