from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != 'O':
                return
            board[r][c] = '#'  # 標記為安全
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        # 1. 從邊界開始 DFS
        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)
        for j in range(n):
            dfs(0, j)
            dfs(m-1, j)

        # 2. 轉換
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'  # 被包圍
                elif board[i][j] == '#':
                    board[i][j] = 'O'  # 還原


if __name__ == "__main__":
    
    s = Solution()
    question_list = [
        {
            "input": [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]], 
            "output": [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
        },
        {
            "input": [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]],
            "output": [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
        }
    ]

    for question in question_list:
        input_data = question["input"]
        expected_output = question["output"]
        
        s.solve(input_data)  # 修改 in-place
        
        print(f"[{input_data == expected_output}] input: {question['input']}, output: {input_data}, expected: {expected_output}")
