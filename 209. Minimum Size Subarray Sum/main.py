
from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        n = len(nums)
        left = 0
        current_sum = 0
        min_length = 0
        
        for right in range(n):
            current_sum += nums[right]
            
            while current_sum >= target: # 代表已經滿足要素（嘗試搜縮左邊邊界）
                if min_length == 0 or (right - left + 1) < min_length:
                    min_length = right - left + 1
                current_sum -= nums[left]
                left += 1
                
        return min_length if min_length > 0 else 0
        
        
        
if __name__ == "__main__":
    
    s = Solution()
    question_list = [
        {"input": [7, [2, 3, 1, 2, 4, 3]], "output": 2},
        {"input": [4, [1, 4, 4]], "output": 1}
    ]
    
    for question in question_list :
        input_data = question["input"]
        expected_output = question["output"]
        result = s.minSubArrayLen(*input_data)

        print(f"[{result == expected_output}] input: {input_data}, output: {result}, expected_output: {expected_output}")