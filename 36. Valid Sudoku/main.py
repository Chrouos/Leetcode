from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # 追蹤結構
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                
                if num == '.': continue # dont consider about the empty cell
                box_index = (i // 3) * 3 + (j // 3)

                if (num in rows[i]) or (num in cols[j]) or (num in boxes[box_index]):
                    return False

                rows[i].add(num)
                cols[j].add(num)
                boxes[box_index].add(num)

        return True

if __name__ == "__main__":
    s = Solution()
    
    question_list = [
        {
            "input": [
                [
                    ["5","3",".",".","7",".",".",".","."],
                    ["6",".",".","1","9","5",".",".","."],
                    [".","9","8",".",".",".",".","6","."],
                    ["8",".",".",".","6",".",".",".","3"],
                    ["4",".",".","8",".","3",".",".","1"],
                    ["7",".",".",".","2",".",".",".","6"],
                    [".","6",".",".",".",".","2","8","."],
                    [".",".",".","4","1","9",".",".","5"],
                    [".",".",".",".","8",".",".","7","9"]
                ]
            ],
            "output": True
        }
    ]
    
    
    for question in question_list:
        input_data = question["input"]
        expected_output = question["output"]
        
        result = s.isValidSudoku(*input_data)
        
        print(f"[{result == expected_output}] input: {input_data}, output: {result}, expected_output: {expected_output}")