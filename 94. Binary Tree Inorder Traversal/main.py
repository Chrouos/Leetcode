from typing import Optional, List

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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []
        
        result = []
        def dfs(node):
            if not node: return
            dfs(node.left)    # 遍歷左子樹
            result.append(node.val)  # 訪問當前節點
            dfs(node.right)   # 遍歷右子樹

        dfs(root)
        return result
        
if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": [1, None, 2, 3], "output": [1,3,2]},
        {"input": [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9], "output": [4,2,6,5,7,1,3,9,8]}
    ]
    
    
    for question in question_list:
        root = TreeNode().list_to_tree(question['input'])
        
        output = s.inorderTraversal(root)
        print(f"[{output == question['output']}] input: {question['input']}, output: {output}, expected: {question['output']}")