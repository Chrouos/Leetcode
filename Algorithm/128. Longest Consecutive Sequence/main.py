
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        給定一個整數數組 nums，找出其中最長的連續元素序列的長度。
        例如，對於 nums = [100, 4, 200, 1, 3, 2]，最長的連續序列是 [1, 2, 3, 4]，其長度為 4。
        '''
        
        num_set = set(nums)
        longest_streak = 0
        
        for num in num_set:
            # 只從序列的起點開始計算
            if num - 1 not in num_set: 
                current_num = num
                current_streak = 1
                
                # 向後查找連續的數字
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                longest_streak = max(longest_streak, current_streak)
                
        return longest_streak


if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": [[100, 4, 200, 1, 3, 2]], "output": 4}, 
        {"input": [[0, 0, 1, 1, 2, 2]], "output": 3},
    ]
    for question in question_list:
        input_data = question["input"]
        expected_output = question["output"]
        
        result = s.longestConsecutive(*input_data)
        print(f"[{result == expected_output}] input: {input_data}, output: {result}, expected_output: {expected_output}")