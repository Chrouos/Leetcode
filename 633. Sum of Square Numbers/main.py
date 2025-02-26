class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        # 是否為 a^2 + b^2 = c
        
        if c < 0: return False
        
        left, right = 0, int(c ** 0.5)
        while left <= right:
            sum = left * left + right * right
            
            if sum == c: return True
            elif sum < c: left += 1
            else: right -= 1
            
        return False
    
if __name__ == "__main__":
    # Example usage
    solution = Solution()
    question_list = [
        {"input": 5, "output": True},
        {"input": 3, "output": False},
        {"input": 4, "output": True},
        {"input": 2, "output": True},
        {"input": 1, "output": True},
        {"input": 0, "output": True},
    ]
    
    for question in question_list:
        expected = question["output"]
        result = solution.judgeSquareSum(question["input"])
        print(f"[{expected == result}] input: {question['input']} expected: {expected}, result: {result}")
        