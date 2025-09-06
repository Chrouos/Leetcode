from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
    
        if not digits:
            return []

        digit_to_char = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        def backtrack(index: int, path: str):
            if index == len(digits):
                combinations.append(path)
                return
            
            possible_chars = digit_to_char[digits[index]]
            for char in possible_chars:
                backtrack(index + 1, path + char)

        combinations = []
        backtrack(0, "")
        return combinations

if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": "23", "output": ["ad","ae","af","bd","be","bf","cd","ce","cf"]},
        {"input": "", "output": []},
        {"input": "2", "output": ["a","b","c"]},
    ]
        
        
    for question in question_list:
        input_data = question["input"]
        expected_output = question["output"]

        result = s.letterCombinations(input_data)
        print(f"[{result == expected_output}] input: {input_data}, output: {result}, expected_output: {expected_output}")