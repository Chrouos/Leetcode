class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if s == "": return ""
        elif len(s) == 1: return s
        
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        
        longest = ""
        for i in range(len(s)):
            odd = expandAroundCenter(i, i)
            even = expandAroundCenter(i, i+1)
            longest = max(longest, odd, even, key=len)
            
        return longest
    
        
        


if __name__ == '__main__':
    s = Solution()
    
    question_list = [
        {"input": "babad", "output": "bab"},
        {"input": "cbbd", "output": "bb"},
        {"input": "abdksiwissi", "output": "siwis"},
    ]
    
    for question in question_list:
        print(s.longestPalindrome(question['input']), question['output'])
    