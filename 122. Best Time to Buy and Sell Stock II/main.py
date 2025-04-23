from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit

if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": [7, 1, 5, 3, 6, 4], "output": 7},
        {"input": [1, 2, 3, 4, 5], "output": 4},
        {"input": [7, 6, 4, 3, 1], "output": 0},
        
    ]
    
    for question in question_list:
        input_data = question["input"]
        expected_output = question["output"]
        
        # Call the function with the input data
        result = s.maxProfit(input_data)
        print(f"[{result == expected_output}] input: {input_data}, output: {result}, expected_output: {expected_output}")