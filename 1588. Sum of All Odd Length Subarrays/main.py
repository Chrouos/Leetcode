from typing import List

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        n = len(arr)
        total = 0
        for i in range(n):
            left_count = i + 1  
            right_count = n - i 
            odd_count = ((left_count * right_count) + 1) // 2
            total += arr[i] * odd_count 
        
        return total

    
if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": [1, 4, 2, 5, 3], "output": 58},
        {"input": [1, 2], "output": 3},
        {"input": [10, 11, 12], "output": 66},
    ]
    
    for question in question_list:
        expected = question["output"]
        result = s.sumOddLengthSubarrays(question["input"])
        print(f"[{result == expected}] input: {question['input']}, output: {result}, expected: {expected}")