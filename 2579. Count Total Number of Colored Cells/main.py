class Solution:
    def coloredCells(self, n: int) -> int:
        
        new = 4
        dp = [0] * (n + 1)
        dp[1] = 1
        
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + new
            new += 4
            
        return dp[n]
    
    def quick_colorCells(self, n: int) -> int:
        return 2 * n * (n - 1) + 1

if __name__ == "__main__":
    sol = Solution()
    question_list = [
        {"input": 1, "output": 1},
        {"input": 2, "output": 5},
        {"input": 3, "output": 13}
    ]
    
    for question in question_list:
        output = sol.quick_colorCells(question["input"])
        print(f"[{output == question['output']}] input: {question['input']}, output: {output}, expected: {question['output']}")