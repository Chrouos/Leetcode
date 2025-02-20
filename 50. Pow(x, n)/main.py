class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        # 任何次方 n 的 0 次方都是 1
        if n == 0: return 1  
        
        if n < 0:
            x = 1 / x  
            n = -n

        result = 1
        while n > 0:
            if n % 2 == 1:
                result *= x
            x *= x 
            n //= 2 
            print(f"result: {result}, x: {x}, n: {n}")
        
        return result

if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": [2.00000, 10], "output": 1024.00000},
        {"input": [2.10000, 3], "output": 9.26100},
        {"input": [2.00000, -2], "output": 0.25000}
    ]
    
    for question in question_list:
        result = s.myPow(*question["input"])
        print(f"[ANS] result: {result}, expected: {question['output']}")
        assert abs(result - question["output"]) < 1e-5, "Wrong Answer!"
