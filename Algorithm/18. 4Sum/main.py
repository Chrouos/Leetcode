from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        

if __name__ == "__main__":
    
    s = Solution()
    question_list = [
        {"input": [[1,0,-1,0,-2,2], 0], "output": [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]},
        {"input": [[], 0], "output": []},
        {"input": [[2,2,2,2,2], 8], "output": [[2,2,2,2]]}
    ]
    
    for question in question_list:
        input_data = question["input"]
        expected_output = question["output"]
        
        result = s.fourSum(input_data[0], input_data[1])
        print(f"[{result == expected_output}] input: {input_data}, output: {result}, expected_output: {expected_output}")