class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        
        result = []
        def parenthesis(s, left_count, right_count):
            if left_count == 0 and right_count == 0:
                result.append(s)
            if left_count > 0:
                parenthesis(s + '(', left_count - 1, right_count)
            if right_count > left_count:
                parenthesis(s + ')', left_count, right_count - 1)        
        
        parenthesis('', n, n)
        return result
        

if __name__ == '__main__':
    n_list = [3, 1]
    s = Solution()
    
    for n in n_list:
        print(s.generateParenthesis(n))