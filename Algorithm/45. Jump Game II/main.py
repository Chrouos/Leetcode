from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        
        jumps = 0
        current_end = 0
        farthest = 0
        
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
                
        return jumps
    
if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": [2, 3, 1, 1, 4], "output": 2},
        {"input": [2, 3, 0, 1, 4], "output": 2},
        {"input": [0], "output": 0},
        {"input": [1], "output": 0},
        {"input": [2, 0], "output": 1},
        {"input": [2, 0, 0], "output": 1},
    ]
    
    for question in question_list:
        input_data = question["input"]
        expected_output = question["output"]
        
        # Call the function with the input data
        result = s.jump(input_data)
        print(f"[{result == expected_output}] input: {input_data}, output: {result}, expected_output: {expected_output}")