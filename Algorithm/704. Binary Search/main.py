from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return left if nums[left] == target else -1
    
if __name__ == "__main__":
    solution = Solution()
    
    question_list = [
        # {"input": [[-1,0,3,5,9,12], 9], "output": 4},
        {"input": [[-1,0,3,5,9,12], 2], "output": -1},
        {"input": [[-1,0,3,5,9,12], 13], "output": -1},
    ]
    
    for question in question_list:
        result = solution.search(*question["input"])
        print(f"[{result == question['output']}], input: {question['input']}")
        