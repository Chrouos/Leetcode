class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        
        # 轉換成 3 進位
        while n > 0:
            if n % 3 == 2: return False # 3進位的數字中，不能有 2
            n //= 3
        
        return True
        
        
        
        
        
if __name__ == "__main__":
    sol = Solution()
    question_list = [
        {"input": 12, "output": True},
        {"input": 91, "output": True},
        {"input": 21, "output": False},
    ]
    
    for question in question_list:
        output = sol.checkPowersOfThree(question["input"])
        print(f"[{output == question['output']}] input: {question['input']}, output: {output}, expected: {question['output']}")