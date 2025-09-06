from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        small_num = prices[0]
        max_profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] < small_num:
                small_num = prices[i]
            elif prices[i] - small_num > max_profit:
                max_profit = prices[i] - small_num
        return max_profit

if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": [7, 1, 5, 3, 6, 4], "output": 5},
        {"input": [7, 6, 4, 3, 1], "output": 0},
        {"input": [2, 1], "output": 0},
        {"input": [1, 2], "output": 1},
        {"input": [2, 4, 1], "output": 2},
        {"input": [2, 4, 3], "output": 2},
        {"input": [2, 4, 5], "output": 3},
    ]
    
    for question in question_list:
        input_data = question["input"]
        expected_output = question["output"]
        
        # Call the function with the input data
        result = s.maxProfit(input_data)
        print(f"[{result == expected_output}] input: {input_data}, output: {result}, expected_output: {expected_output}")