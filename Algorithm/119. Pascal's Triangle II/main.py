from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1]]
        for i in range(1, rowIndex+1):
            add_lens = len(res[i-1]) - 1
            result = [1] + [res[i-1][j] + res[i-1][j+1] for j in range(add_lens)] + [1]
            res.append(result)
        return res[rowIndex]
        
if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": 3, "output": [1,3,3,1]},
        {"input": 0, "output": [1]},
        {"input": 1, "output": [1,1]},
    ]
    
    for question in question_list:
        output = s.getRow(question['input'])
        print(f"[{question['output'] == output}] input: {question['input']}, output: {output}, expected: {question['output']}")