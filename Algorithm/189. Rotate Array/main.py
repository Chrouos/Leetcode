from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        if k == 0:
            return
        
        nums_copy = nums.copy()
        n = len(nums)
        k %= n 
        
        for i in range(n):
            nums[i] = nums_copy[(i - k) % n]
            
if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": [1,2,3,4,5,6,7], "k": 3, "output": [5,6,7,1,2,3,4]},
        {"input": [-1,-100,3,99], "k": 2, "output": [3,99,-1,-100]},
        {"input": [1,2], "k": 3, "output": [2,1]},
        {"input": [1], "k": 0, "output": [1]},
        {"input": [], "k": 0, "output": []},
    ]
    
    for question in question_list:
        result = question["input"].copy()
        s.rotate(result, question["k"])
        print(f"[{question['output'] == result}] input: {question['input']}, k: {question['k']}, output: {result}")