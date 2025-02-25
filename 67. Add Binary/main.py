class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        
        while i >= 0 or j >= 0 or carry:
            num_a = int(a[i]) if i >= 0 else 0
            num_b = int(b[j]) if j >= 0 else 0
            
            # divmod 計算進位與當前位數
            carry, digit = divmod(num_a + num_b + carry, 2)
            result.append(str(digit))
            i -= 1
            j -= 1
        
        return "".join(result[::-1])
        
                
if __name__ == "__main__":
    
    s = Solution()
    question_list = [
        {"input": ["11", "1"], "output": "100"},
        {"input": ["1010", "1011"], "output": "10101"},
    ]
    for question in question_list:
        result = s.addBinary(*question["input"])
        print(f"[{result == question['output']}] {result} =? {question['output']}")
        