from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        n = len(grid)
        
        dp = [0] * (n * n + 1)
        total_count = (n * n) * (n * n + 1) // 2
        result = [0, 0]
        
        # find the repeat
        for i in range(n):
            for j in range(n):
                dp[grid[i][j]] += 1
                total_count -= grid[i][j]
                
                if dp[grid[i][j]] == 2:
                    result[0] = grid[i][j]
        
        # missing value
        result[1] = total_count + result[0]
        return result
                
                
if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": [[[1,2,3],[4,5,6],[7,8,9]]], "output": [0, 0]},
        {"input": [[[1,3],[2,2]]], "output": [2, 4]},
        {"input": [[[9,1,7],[8,9,2],[3,4,6]]], "output": [9,5]},
    ]
    
    for question in question_list:
        output = s.findMissingAndRepeatedValues(question['input'][0])
        print(f"[{output == question['output']}] input: {question['input']}, output: {output}, expected: {question['output']}")