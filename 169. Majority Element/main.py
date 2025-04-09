from typing import List
class Solution:
    
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
        
        
    # def majorityElement(self, nums: List[int]) -> int:
    #     count = 0
    #     candidate = None

    #     for num in nums:
    #         if count == 0:
    #             candidate = num
    #         count += (1 if num == candidate else -1)

    #     return candidate

    
if __name__ == "__main__":
    
    s = Solution()
    question_list = [
        {"input": [3,2,3], "output": 3},
        {"input": [2,2,1,1,1,2,2], "output": 2},
    ]
    
    for question in question_list:
        result = s.majorityElement(question["input"])
        print(f"[{question['output'] == result}] input: {question['input']}, output: {result}")
            
            
                