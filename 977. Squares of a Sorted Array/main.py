from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        return sorted([x * x for x in nums])
        
        
if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": [-4,-1,0,3,10], "output": [0,1,9,16,100]},
    ]
    
    for question in question_list:
        output = s.sortedSquares(question["input"])
        print(f"[{output == question['output']}] input: {question['input']}, output: {output}, expected: {question['output']}")