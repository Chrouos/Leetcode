class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        i = 0
        n = len(s)
        result = 0
        sign = 1

        # 1. 跳過前導空格
        while i < n and s[i] == ' ':
            i += 1

        # 2. 處理符號
        if i < n and (s[i] == '-' or s[i] == '+'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # 3. 讀取數字
        while i < n and s[i].isdigit():
            digit = int(s[i])

            # 4. 檢查溢出
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            i += 1

        return result * sign

    
if __name__ == '__main__':
    s = Solution()
    question_list = [
        {"input": "42", "output": 42},
        {"input": "   -42", "output": -42},
        {"input": "4193 with words", "output": 4193},
        {"input": "words and 987", "output": 0},
        {"input": "-91283472332", "output": -2147483648},
        {"input": "0-1", "output": 0},
        {"input": "3.14159", "output": 3},
        {"input": "21474836460", "output": 2147483647},
        {"input": "  0000000000012345678", "output": 12345678},
        {"input": "  00000000000", "output": 0},
    ]
    
    for question in question_list:
        print(s.myAtoi(question["input"]) == question["output"], s.myAtoi(question["input"]), question["output"])
    