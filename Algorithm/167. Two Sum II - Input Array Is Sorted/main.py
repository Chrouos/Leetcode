from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left, right = 0, len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        
        return []
        
        
if __name__ == "__main__":
    
    s = Solution()
    question_list = [
        {"input": [[2, 7, 11, 15], 9], "output": [1, 2]},
        {"input": [[2, 3, 4], 6], "output": [1, 3]},
        {"input": [[-1, 0], -1], "output": [1, 2]},
        {"input": [[], 0], "output": []},
        {"input": [[1, 2, 3], 5], "output": [2, 3]},
        {"input": [[1, 2, 3, 4, 5], 9], "output": [4, 5]},
    ]
    
    for question in question_list:
        input_data = question["input"]
        expected_output = question["output"]

        # Call the function with the input data
        result = s.twoSum(*input_data)
        print(f"[{result == expected_output}] input: {input_data}, output: {result}, expected_output: {expected_output}")