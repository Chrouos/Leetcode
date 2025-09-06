class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        # true if num is a perfect square
        if num < 2: return True
        
        left, right = 2, num // 2
        while left < right:
            mid = ( left + right ) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                left = mid + 1
            else:
                right = mid
                
        return left * left == num
    
if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": 16, "output": True},
        {"input": 14, "output": False},
        {"input": 1, "output": True},
        {"input": 0, "output": True},
        {"input": 4, "output": True},
    ]
    
    for question in question_list:
        expected = question["output"]
        result = s.isPerfectSquare(question["input"])
        print(f"[{expected == result}] input: {question['input']} expected: {expected}, result: {result}")
    