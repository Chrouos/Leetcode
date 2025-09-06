class Solution:
    def reverse(self, x: int) -> int:
        
        result = 0
        sign = 1 if x > 0 else -1
        
        x = abs(x)
        while x != 0:
            result = result * 10 + x % 10
            x = x // 10
            
        if result > 2**31 - 1 or result < -2**31:
            return 0
            
        return result * sign
            
        

if __name__ == '__main__':
    
    s = Solution()
    question_list = [
        {"input": 123, "output": 321},
        {"input": -123, "output": -321},
        {"input": 120, "output": 21},
        {"input": 0, "output": 0},
    ]
    
    for question in question_list:
        print(s.reverse(question['input']), question['output'])
    

