class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # s = ''.join(c.lower() for c in s if c.isalnum())
        s = ''.join(filter(str.isalnum, s)).lower()
        return s == s[::-1]
        

if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": "A man, a plan, a canal: Panama", "output": True},
        {"input": "race a car", "output": False},
        {"input": " ", "output": True},
    ]
    
    for question in question_list:
        input_data = question["input"]
        expected_output = question["output"]
        
        # Call the function with the input data
        result = s.isPalindrome(input_data)
        print(f"[{result == expected_output}] input: {input_data}, output: {result}, expected_output: {expected_output}")