
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        '''
        Reverse Polish Notation (RPN) 是一種後綴表示法，給定一個 RPN 表達式，計算其值。
        3 + 4 => 3 4 +
        '''
        
        stack = []
        operators = {"+": lambda x, y: x + y, "-": lambda x, y: x - y, "*": lambda x, y: x * y, "/": lambda x, y: int(x / y)}
        
        for token in tokens:
            if token in operators:
                b = stack.pop()
                a = stack.pop()
                result = operators[token](a, b)
                stack.append(result)
            else:
                stack.append(int(token))
                
        return stack[0] if stack else 0
        
        
if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": [["2","1","+","3","*"]], "output": 9},
        {"input": [["4","13","5","/","+"]], "output": 6},
        {"input": [["10","6","9","3","+","-11","*","/","*","17","+","5","+"]], "output": 22},
        {"input": [["3","-4","+"]], "output": -1},
    ]
    
    for question in question_list:
        input_data = question["input"]
        expected_output = question["output"]
        
        result = s.evalRPN(*input_data)
        print(f"[{result == expected_output}] input: {input_data}, output: {result}, expected_output: {expected_output}")