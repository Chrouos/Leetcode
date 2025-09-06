# The isBadVersion API is already defined for you.


class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        left = 1
        right = n
        
        # 往中間找，先錯了就往前找
        while left != right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
            
        return left
        
if __name__ == '__main__':
    s = Solution()
    question_list = [
        {"input": 5, "bad": 4, "output": 4},
        {"input": 1, "bad": 1, "output": 1},
        {"input": 2, "bad": 1, "output": 1},
        {"input": 2126753390, "bad": 1702766719, "output": 1702766719},
    ]
    
    for question in question_list:
        def isBadVersion(version: int) -> bool:
            return version >= question['bad']
        print(s.firstBadVersion(question['input']) == question['output'])
    
    