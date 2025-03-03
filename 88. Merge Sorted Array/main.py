from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        result = []
        i, j = 0, 0
        
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1
                
        result.extend(nums1[i:m])
        result.extend(nums2[j:n])
        nums1[:m+n] = result

if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": [[1,2,3,0,0,0], 3, [2,5,6], 3], "output": [1,2,2,3,5,6]},
        # {"input": [[1], 1, [], 0], "output": [1]},
        # {"input": [[0], 0, [1], 1], "output": [1]},
    ]
    
    for question in question_list:
        output = s.merge(*question["input"])
        print(f"[{output == question['output']}] input: {question['input']}, output: {output}, expected: {question['output']}")