class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: return x
        
        left, right = 2, x // 2
        while left <= right:
            mid = ( left + right ) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
                
        return right
    
if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": 4, "output": 2},
        {"input": 8, "output": 2},
        {"input": 16, "output": 4},
        {"input": 1, "output": 1},
        {"input": 0, "output": 0},
        {"input": 169, "output": 13},
    ]
    
    for question in question_list:
        expected = question["output"]
        result = s.mySqrt(question["input"])
        print(f"[{expected == result}] input: {question['input']} expected: {expected}, result: {result}")