from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
        return True
    
if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": [2, 3, 1, 1, 4], "output": True},
        {"input": [3, 2, 1, 0, 4], "output": False},
        {"input": [0], "output": True},
        {"input": [1], "output": True},
        {"input": [2, 0], "output": True},
        {"input": [2, 0, 0], "output": True},
    ]
    
    for question in question_list:
        input_data = question["input"]
        expected_output = question["output"]
        
        # Call the function with the input data
        result = s.canJump(input_data)
        print(f"[{result == expected_output}] input: {input_data}, output: {result}, expected_output: {expected_output}")