from typing import Optional, List

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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    
        if root is None: return []
        
        result = []
        def dfs(node, depth):
            if node is None: return
            
            if depth == len(result):
                result.append(node.val)

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return result