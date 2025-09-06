
from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
        一個數組 nums 中的相同數字 (nums[i] == nums[j]) 是否存在索引 i 和 j，使得它們的差的絕對值小於等於 k (|i - j| <= k)。
        如果存在這樣的索引對，則返回 True；否則返回 False。
        '''
        
        
        nums_dict = {}
        for i, num in enumerate(nums):
            if num in nums_dict and i - nums_dict[num] <= k:
                return True
            nums_dict[num] = i
        return False
        


if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": [[1, 2, 3, 1], 3], "output": True},
        {"input": [[1, 0, 1, 1], 1], "output": True},
        {"input": [[1, 2, 3, 1, 2, 3], 2], "output": False},
    ]
    
    for question in question_list:
        input_data = question["input"]
        expected_output = question["output"]
        
        result = s.containsNearbyDuplicate(*input_data)
        print(f"[{result == expected_output}] input: {input_data}, output: {result}, expected_output: {expected_output}")