class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0: return False # Negative numbers are not palindromes (e.g. -121)
        
        # To check if a number is a palindrome, we only need to check half of the digits
        for i in range(len(str(x)) // 2): 
            
            # If the digits are not the same, the number is not a palindrome
            if str(x)[i] != str(x)[len(str(x)) - i - 1]: return False 
            
        return True


if __name__ == '__main__':
    xs = [121, -121, 10, -101]
    for x in xs:
        print(Solution().isPalindrome(x))