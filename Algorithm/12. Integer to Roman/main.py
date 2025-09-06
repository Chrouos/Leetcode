class Solution:
    def intToRoman(self, num: int) -> str:
        
        roman_dict = {
            1000: "M", 
            900: "CM", 
            500: "D", 
            400: "CD",
            100: "C", 
            90: "XC", 
            50: "L", 
            40: "XL",
            10: "X", 
            9: "IX", 
            5: "V", 
            4: "IV",
            1: "I"
        }
        
        result_roman = ""
        for value, symbol in roman_dict.items():
            while num >= value:
                num -= value
                result_roman += symbol
        return result_roman
            
            
if __name__ == '__main__':
    
    s = Solution()
    question_list = [
        {"input": 3749, "output": "MMMDCCXLIX"},
        {"input": 3, "output": "III"},
        {"input": 58, "output": "LVIII"},
        {"input": 1994, "output": "MCMXCIV"},
        
    ]
    
    for question in question_list:
        print(f"input: {question['input']} => {s.intToRoman(question['input']) == question['output']}")
        
        