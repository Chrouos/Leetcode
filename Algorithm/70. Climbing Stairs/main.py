class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1: return 1
        elif n == 2: return 2
        else:
            dp = [0] * (n + 1)
            dp[1] = 1
            dp[2] = 2
            for i in range(3, n + 1):
                dp[i] = dp[i - 1] + dp[i - 2]
                
            return dp[n]
        
if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": 2, "output": 2},
        {"input": 3, "output": 3},  
        {"input": 4, "output": 5},
        {"input": 5, "output": 8},
        {"input": 6, "output": 13},
    ]
    
    for question in question_list:
        output = s.climbStairs(question["input"])
        print(f"[{output == question['output']}] input: {question['input']}, output: {output}, expected: {question['output']}")