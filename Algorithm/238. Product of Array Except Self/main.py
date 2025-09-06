from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        result = [1] * n
        left_product = 1
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]
        
        right_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]
        return result
        
if __name__ == "__main__":
    sol = Solution()
    question_list = [
        {"input": [1, 2, 3, 4], "output": [24, 12, 8, 6]},
        {"input": [-1, 1, 0, -3, 3], "output": [0, 0, 9, 0, 0]},
        {"input": [1], "output": [1]},
        {"input": [1, 2], "output": [2, 1]},
    ]
    
    for question in question_list:
        input_data = question["input"]
        expected_output = question["output"]
        
        # Call the function with the input data
        result = sol.productExceptSelf(input_data)
        print(f"[{result == expected_output}] input: {input_data}, output: {result}, expected_output: {expected_output}")