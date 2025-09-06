from typing import List
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        
        Conway’s Game of Life
        """
        
        '''
        Rules:
        
        1 : Live cell
        0 : Dead cell

        1. Live cell with Live neighbors < 2 dies (underpopulation) 
        2. Live cell with Live neighbors > 3 dies (overpopulation)
        3. Live cell with Live neighbors == 2 or 3 lives on to the
        4. Dead cell with Live neighbors == 3 becomes a live cell (reproduction)
        
        updated board in same time.
        in-place update:
        '''
        
        
        '''
        Method:
        
        O(1) space complexity by using the original board to store the next state.
        2: Live cell that will die in the next state
        -1: Dead cell that will become live in the next state
        '''
        
        rows, cols = len(board), len(board[0])
        
            
        
        
        
if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": [[0, 1], [1, 0]], "output": [[1, 0], [0, 1]]},
        {"input": [[1, 1], [1, 0]], "output": [[1, 1], [1, 1]]},
        {"input": [[0]], "output": [[0]]},
        {"input": [[1]], "output": [[0]]}
    ]
    
    for question in question_list:
        input_board = question["input"]
        expected_output = question["output"]
        
        # Call the function with the input data
        s.gameOfLife(input_board)
        print(f"[{input_board == expected_output}] Input: {input_board}, Output: {input_board}, Expected: {expected_output}")