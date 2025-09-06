
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        '''
        目標總和 = 0 → nums[i] + nums[l] + nums[r] == 0
        '''
        
        result = []
        nums.sort()
        
        for i in range(len(nums) - 2 ):
            if i > 0 and nums[i] == nums[i - 1]: continue # 如果在排序中遇到重複的數值就跳過
            
            l, r = i + 1, len(nums) - 1
            while l < r :
                total = nums[i] + nums[l] + nums[r]
                
                #. skip the numbers
                if total < 0 : # 代表數字小了，需要往右
                    l += 1
                elif total > 0: # 代表數字大了，需要往左
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                
                    #. skip the repeat
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    
                    l += 1
                    r -= 1
                
        return result
                

if __name__ == "__main__":
    
    s = Solution()
    question_list = [
        {"input": [-1,0,1,2,-1,-4], "output": [[-1,-1,2],[-1,0,1]]},
        {"input": [0,1,1], "output": []},
    ]
    
    for question in question_list:
        input_data = question["input"]
        expected_output = question["output"]
        
        result = s.threeSum(input_data)
        print(f"[{result == expected_output}] Input: {input_data}, Output: {result}, Expected: {expected_output}")