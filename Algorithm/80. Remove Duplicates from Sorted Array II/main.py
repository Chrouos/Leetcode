
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        max_times = 2

        for num in nums:
            if index < max_times or num != nums[index-max_times]:
                nums[index] = num
                index += 1
                
        return index

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
        
#         last_num = nums[0]
#         last_num_count = 1
#         move_count = 0

#         lengths = len(nums)
#         current_index = 1
#         while current_index + move_count < lengths:
            
#             if nums[current_index] == last_num: 
#                 last_num_count += 1
            
#             elif nums[current_index + move_count] != last_num:
#                 last_num_count = 1
                
#             if last_num_count > 2:
#                 nums[current_index] = None
#                 move_count += 1
                
#             if nums[current_index] is None:
                
#                 if current_index + move_count >= lengths:
#                     nums[current_index] = None
#                     break
#                 # print(f"before: {nums}")
#                 nums[current_index] = nums[current_index + move_count]
#                 nums[current_index + move_count] = None
#                 # print(f"after : {nums}")
#                 # print(f"cuuent_index: {current_index}, move_count: {move_count}, last_num_count: {last_num_count}, last_num: {last_num}\n")
#                 current_index -= 1
                
#             last_num = nums[current_index]
                
                
#             current_index += 1
#             # print(f"current_index: {current_index}, move_count: {move_count}, last_num_count: {last_num_count}, nums: {nums}")
        
#         return lengths - move_count

if __name__ == "__main__":
    
    s = Solution()
    question_list = [
        {"input": [1,1,1,2,2,3], "output": 5},
        {"input": [0,0,1,1,1,1,2,3,3], "output": 7},
        {"input": [1,1,1], "output": 2},
        {"input": [1,1,1,2,2,2,3,3], "output": 6},
    ]    
    
    for question in question_list:
        result = s.removeDuplicates(question['input'])
        print(f"[{result == question['output']}], input: {question['input']}")