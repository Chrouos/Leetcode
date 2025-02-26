from typing import List

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
    
        n = len(nums)
        return sum( x * x for i, x in enumerate(nums) if ( n % ( i + 1 ) == 0 ) )
    
if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": [1, 2, 3, 4], "output": 21},
        {"input": [2, 7, 1, 19, 18, 3], "output": 63},
    ]
    for question in question_list:
        expected = question["output"]
        result = s.sumOfSquares(question["input"])
        print(f"[{expected == result}] input: {question['input']} expected: {expected}, result: {result}")