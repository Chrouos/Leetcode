from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if len(nums) == 0: return 0
        
        count = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[count]:
                count += 1
                nums[count] = nums[i]
        
        return count + 1
        
if __name__ == '__main__':
    nums_list = [[1, 1, 2], [0,0,1,1,1,2,2,3,3,4]]
    s = Solution()
    
    for nums in nums_list:
        print(s.removeDuplicates(nums))