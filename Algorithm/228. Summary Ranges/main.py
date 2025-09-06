
from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        '''
        給訂一個數組，若有連續的部分，則將其表示為範圍。
        例如，對於 nums = [0, 1, 2, 4, 5, 7]，返回 ["0->2", "4->5", "7"]。
        如果數字不連續，則單獨返回該數字
        '''
        
        if not nums: return []
        elif len(nums) == 1: return [str(nums[0])]
        
        ranges = []
        start = nums[0]
        
        for i in range(1, len(nums)):
            # 如果當前數字不是前一個數字加1，則表示連續序列結束
            if nums[i] != nums[i - 1] + 1: 
                if start == nums[i - 1]: ranges.append(str(start)) # 如果只有一個數字，則直接添加
                else: ranges.append(f"{start}->{nums[i - 1]}") # 如果有連續的數字，則添加範圍
                start = nums[i]
            
            # 如果是最後一個數字，則需要處理
            if i == len(nums) - 1:
                if start == nums[i]: ranges.append(str(start))
                else: ranges.append(f"{start}->{nums[i]}")
                
        return ranges

if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": [[0, 1, 2, 4, 5, 7]], "output": ["0->2", "4->5", "7"]},
        {"input": [[0, 2, 3, 4, 6, 8, 9]], "output": ["0", "2->4", "6", "8->9"]},
        {"input": [[-1]], "output": ["-1"]},
        {"input": [[-1, 0, 1, 2, 4, 5, 7]], "output": ["-1->2", "4->5", "7"]},
        {"input": [[1, 3]], "output": ["1", "3"]},
        {"input": [[1, 2, 3]], "output": ["1->3"]},
    ]
    
    for question in question_list: 
        input_data = question["input"]
        expected_output = question["output"]
        
        result = s.summaryRanges(*input_data)
        print(f"[{result == expected_output}] input: {input_data}, output: {result}, expected_output: {expected_output}")