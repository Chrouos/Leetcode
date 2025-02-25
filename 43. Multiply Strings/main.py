class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        if num1 == "0" or num2 == "0": return "0"
        
        # ord: 取得單一字元對應的 ASCII 或 Unicode 數值
        result = 0
        for i_1 in range(-1, -len(num1)-1, -1):
            int_n1 = (ord(num1[i_1]) - ord("0")) * 10**(-i_1-1)
            # print(f"int_n1: {int_n1}")
            
            for i_2 in range(-1, -len(num2)-1, -1):
                int_n2 = (ord(num2[i_2]) - ord("0")) * 10**(-i_2-1)
                # print(f"int_n2: {int_n2}")
                result += int_n1 * int_n2
                
        return str(result)
        
if __name__ == "__main__":
    s = Solution()
    
    question_list = [
        {"input": ["2", "3"], "output": "6"},
        {"input": ["123", "456"], "output": "56088"},
        {"input": ["0", "0"], "output": "0"},
        {"input": ["0", "1"], "output": "0"},
        {"input": ["1", "0"], "output": "0"},
    ]
    for question in question_list:
        result = s.multiply(*question["input"])
        print(f"[{result == question['output']}] {result} =? {question['output']}")