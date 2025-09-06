from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        '''
        1. 二元搜尋樹 (BST, Binary Search Tree)
        每個節點的左子樹都只包含比該節點小的數字，而右子樹則包含比該節點大的數字

        2. 中序遍歷 (Inorder Traversal) 會得到一個遞增序列
        
        '''
        
        if not nums: return None
        
        mid = len(nums) // 2
        root = TreeNode(nums[mid])  # 選擇中間元素作為根節點
        root.left = self.sortedArrayToBST(nums[:mid])  # 遞迴構造左子樹
        root.right = self.sortedArrayToBST(nums[mid+1:])  # 遞迴構造右子樹
        
        return root
        


if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": [-10,-3,0,5,9], "output": [0,-3,9,-10,None,5]},
        {"input": [1,3], "output": [3,1]},
    ]
    
    for quesiont in question_list:
        output = s.sortedArrayToBST(quesiont['input'])
        print(f"[{quesiont['output'] == output}], input: {quesiont['input']}, output: {output}")
        