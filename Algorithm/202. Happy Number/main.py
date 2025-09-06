class Solution:
    def isHappy(self, n: int) -> bool:
        '''
        給定一個正整數 n，判斷它是否為快樂數。
        快樂數的定義是：對於一個正整數 n，反覆將其各位數字平方後求和，直到得到 1 或者循環出現。
        '''
        
        seen = set() # 用來記錄已經出現過的數字，重複就會無限循環
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))
        return n == 1


if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": [19], "output": True},
        {"input": [2], "output": False},
        {"input": [7], "output": True},
        {"input": [1], "output": True},
        {"input": [4], "output": False},
    ]
    
    for question in question_list:
        input_data = question["input"]
        expected_output = question["output"]
        
        result = s.isHappy(*input_data)
        print(f"[{result == expected_output}] input: {input_data}, output: {result}, expected_output: {expected_output}")