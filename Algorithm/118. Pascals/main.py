from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):
            
            add_lens = len(res[i-1]) - 1 # 需要添加的元素個數，是上一層的元素個數減1
            result = [1] + [res[i-1][j] + res[i-1][j+1] for j in range(add_lens)] + [1]
            res.append(result)
            
        return res
        
        
if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": 5, "output": [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]},
    ]
    
    for question in question_list:
        output = s.generate(question['input'])
        print(f"[{question['output'] == output}] input: {question['input']}, output: {output}, expected: {question['output']}")
