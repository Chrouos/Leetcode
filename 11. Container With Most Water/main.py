
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            current_area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, current_area)
            
            if height[left] < height[right]: left += 1
            else: right -= 1
        
        return max_area
    
if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": [1,8,6,2,5,4,8,3,7], "output": 49},
        {"input": [1,1], "output": 1},
        {"input": [1,8,6,2,5,4,8,3,7], "output": 49},
        {"input": [4,3,2,1,4], "output": 16},
        {"input": [1,2,1], "output": 2},
    ]
    
    for question in question_list:
        print(s.maxArea(question["input"]), question["output"])
        
        
        
        
        