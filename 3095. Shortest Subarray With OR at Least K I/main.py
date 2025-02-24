from typing import List

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        min_length = float('inf') # 代表無限大，如果設置為 0 會無法更新 min_length
        
        curr_or_dict = {} # 記錄所有可能性的 OR 值
        for i in range(n):
            new_or_dict = {nums[i]: 1} # 把自己的當作子陣列 (長度為1)
            
            for prev_or in curr_or_dict:
                combined_or = prev_or | nums[i]
                
                # 如果已經有這個 OR 值，就取最小的長度
                if combined_or in new_or_dict:
                    new_or_dict[combined_or] = min(new_or_dict[combined_or], curr_or_dict[prev_or] + 1)
                
                # 如果沒有這個 OR 值，就新增
                else:
                    new_or_dict[combined_or] = curr_or_dict[prev_or] + 1
                
            curr_or_dict = new_or_dict  # 更新成新的
            
            # 檢查有沒有結果已經達到k
            for or_val, length in curr_or_dict.items():
                if or_val >= k:
                    min_length = min(min_length, length)
                
                    
        return min_length if min_length != float('inf') else -1

if __name__ == "__main__":
    
    s = Solution()
    question_list = [
        {"input": [[1, 2, 3], 2], "output": 1},
        {"input": [[2, 1, 8], 10], "output": 3},
        {"input": [[1, 2], 0], "output": 1},
    ]
    
    for question in question_list:
        print(f"input = {question['input']} => {s.minimumSubarrayLength(*question['input']) == question['output']}")
        
        
'''
Bitwise OR，「按位或運算」

e.g.
    0101  (5的二進位)
|   0011  (3的二進位)
-------
    0111  (結果的二進位) = 7

'''