from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        n = len(citations)
        citations.sort(reverse=True)
        for i in range(n):
            if citations[i] <= i:
                return i
        return n
    
if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": [3, 0, 6, 1, 5], "output": 3},
        {"input": [1, 3, 1], "output": 1},   
        {"input": [1, 2, 3], "output": 2},
        {"input": [0], "output": 0},
        {"input": [1], "output": 1},
        {"input": [2, 0], "output": 1},
        {"input": [2, 0, 0], "output": 1},
    ]
    
    for question in question_list:
        input_data = question["input"]
        expected_output = question["output"]
        
        # Call the function with the input data
        result = s.hIndex(input_data)
        print(f"[{result == expected_output}] input: {input_data}, output: {result}, expected_output: {expected_output}")
        