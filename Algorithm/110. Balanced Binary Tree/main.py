from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def list_to_tree(self, lst):
        if not list: None
        
        root = TreeNode(lst[0])
        queue = [root]
        index = 1
        while queue:
            node = queue.pop(0)
            if node is None: continue
            if index >= len(lst): break
            
            node.left = TreeNode(lst[index]) if lst[index] is not None else None
            queue.append(node.left)
            index += 1
            
            if index >= len(lst): break
            node.right = TreeNode(lst[index]) if lst[index] is not None else None
            queue.append(node.right)
            index += 1
                
        return root

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # 一棵高度平衡（Height-balanced）的二元樹，是指每個節點的左右子樹的高度差不超過 1
        if not root: return True
        
        def dfs(node):
            if not node: return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if left == -1 or right == -1: return -1
            if abs(left - right) > 1: return -1
            return max(left, right) + 1
        
        return dfs(root) != -1
        
if __name__ == "__main__":
    s = Solution()  
    
    question_list = [
        # {"input": [[3,9,20,None,None,15,7]], "output": True},
        {"input": [[1,2,2,3,3,None,None,4,4]], "output": False},
    ]
    for question in question_list:
        p = TreeNode().list_to_tree(question['input'][0])
        
        output = s.isBalanced(p)
        print(f"[{output == question['output']}] input: {question['input']}, output: {output}, expected: {question['output']}")
        
