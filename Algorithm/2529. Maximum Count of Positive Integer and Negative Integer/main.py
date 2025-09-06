from typing import List
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        
        positive_count = 0
        negative_count = 0
        for num in nums:
            if num > 0:
                positive_count += 1
            elif num < 0:
                negative_count += 1
        return max(positive_count, negative_count)
        

if __name__ == "__main__":
    s  = Solution()
    question_list = [
        {"input": [-2,-1,-1,1,2,3], "output": 3},
        {"input": [-3,-2,-1,0,0,1,2], "output": 3},
        {"input": [5,20,66,1314], "output": 4},
        {"input": [-1,-1,-1,-1], "output": 4},
        {"input": [1,2,3,4], "output": 4},
        {"input": [], "output": 0},
    ]
    
    for question in question_list:
        output = s.maximumCount(question['input'])
        print(f"[{question['output'] == output}], input: {question['input']}, output: {output}")