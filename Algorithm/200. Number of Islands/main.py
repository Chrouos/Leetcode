
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        簡單來說：找出有幾座島
        
        解法：
        1. 使用 DFS 或 BFS 遍歷每一個島嶼，並將其標記為已訪問
        2. 計算過的島要變成 '0'，避免重複計數
        '''
        
        if not grid : return 0
        
        m, n = len(grid), len(grid[0]) #= m 為列數, n 為行數
        
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
                return
            
            grid[i][j] = '0'
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
            
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
                    
        return count

if __name__ == "__main__":
    s = Solution()
    
    question_list = [
        {"input": [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ], "output": 1},
        {"input": [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ], "output": 3}, 
    ]
    
    for question in question_list:
        p = question['input']
        output = s.numIslands(p)

        print(f"[{output == question['output']}] input: {question['input']}, output: {output}, expected: {question['output']}")