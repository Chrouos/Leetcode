class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0
        prev = 0
        for char in s:
            if roman_dict[char] > prev:
                result += roman_dict[char] - 2 * prev
            else:
                result += roman_dict[char]
            prev = roman_dict[char]
            
        return result
    
if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt('III')) # 3
    print(s.romanToInt('IV')) # 4
    print(s.romanToInt('IX')) # 9
    print(s.romanToInt('LVIII')) # 58
    print(s.romanToInt('MCMXCIV')) # 1994