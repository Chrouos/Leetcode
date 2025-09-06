from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        if not nums: return 0
        
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        
        return count
        
if __name__ == '__main__':
    question_list = [
        {'nums': [3, 2, 2, 3], 'val': 3, 'answer': 2},
        {'nums': [0, 1, 2, 2, 3, 0, 4, 2], 'val': 2, 'answer': 5}
    ]
    
    s = Solution()
    for question in question_list:
        print(s.removeElement(question['nums'], question['val']))
        