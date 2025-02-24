from typing import List

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def can_rob(cap):
            count = 0
            choose_house = 0
            while choose_house < len(nums):
                if nums[choose_house] <= cap:  # 只能選擇不超過 cap 的房屋
                    count += 1
                    choose_house += 1  
                choose_house += 1  
            return count >= k  # 至少搶到 k 間房屋

        low, high = 0, max(nums) + 1
        while low < high:
            mid = (low + high) // 2
            if can_rob(mid): 
                high = mid
            else:
                low = mid + 1 
                
        return low
            

if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": [[2,3,5,9], 2], "output": 5},
        # {"input": [[2,7,9,3,1], 2], "output": 2},
        # {"input": [[1,2,3,4,5], 1], "output": 1},
        # {"input": [[5038,3053,2825,3638,4648,3259,4948,4248,4940,2834,109,5224,5097,4708,2162,3438,4152,4134,551,3961,2294,3961,1327,2395,1002,763,4296,3147,5069,2156,572,1261,4272,4158,5186,2543,5055,4735,2325,1206,1019,1257,5048,1563,3507,4269,5328,173,5007,2392,967,2768,86,3401,3667,4406,4487,876,1530,819,1320,883,1101,5317,2305,89,788,1603,3456,5221,1910,3343,4597], 28], "output": 4134},
    ]
    
    for question in question_list:
        print(f"input: {question['input']} => result: {s.minCapability(*question['input']) == question['output']}")