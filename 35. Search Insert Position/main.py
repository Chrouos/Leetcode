from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
    
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)
    
    
if __name__ == '__main__':
    s = Solution()
    
    question = [
        {'nums': [1,3,5,6], 'target': 5, 'answer': 2},
        {'nums': [1,3,5,6], 'target': 2, 'answer': 1},
        {'nums': [1,3,5,6], 'target': 7, 'answer': 4},
    ]
    
    for q in question:
        assert s.searchInsert(q['nums'], q['target']) == q['answer']