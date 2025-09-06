class Solution:
    def isValid(self, s: str) -> bool:
        char_stack = []
        char_map = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        
        for c in s:
            if c in char_map:
                if not char_stack or char_stack.pop() != char_map[c]:
                    return False
            else:
                char_stack.append(c)
                
        # If stack is empty, then all the characters are matched
        return not char_stack
        
        
if __name__ == '__main__':
    s = Solution()
    s_list = [
        {"input": "()", "output": True},
        {"input": "()[]{}", "output": True},
        {"input": "(]", "output": False},
        {"input": "([)]", "output": False},
        {"input": "{[]}", "output": True},
        {"input": "]", "output": False},
        {"input": "[", "output": False},
    ]
    
    for i in s_list:
        assert s.isValid(i["input"]) == i["output"]