from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def list_to_tree(lst: List[Optional[int]]) -> Optional['TreeNode']:
        if not lst: return None  # 修正這裡
        
        root = TreeNode(lst[0])
        queue = [root]
        index = 1
        
        while queue:
            node = queue.pop(0)
            if node is None:
                continue

            if index < len(lst):
                node.left = TreeNode(lst[index]) if lst[index] is not None else None
                queue.append(node.left)
                index += 1

            if index < len(lst):
                node.right = TreeNode(lst[index]) if lst[index] is not None else None
                queue.append(node.right)
                index += 1

        return root
    
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = [root]
        depth = 0
        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.pop(0)
                if not node: continue
                if not node.left and not node.right: return depth
                
                queue.append(node.left)
                queue.append(node.right)
                
        return depth
        
        
        # def dfs(node, depth):
        #     if not node: return float('inf')
        #     if not node.left and not node.right: return depth
            
        #     return min(dfs(node.left, depth + 1), dfs(node.right, depth + 1))
        
        # return dfs(root, 1) if root else 0
    
if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": [3, 9, 20, None, None, 15, 7], "output": 2},
        {"input": [2, None, 3, None, 4, None, 5, None, 6], "output": 5},
        {"input": [], "output": 0},
    ]
    
    for question in question_list:
        p = TreeNode().list_to_tree(question['input'])
        
        output = s.minDepth(p)
        print(f"[{output == question['output']}] input: {question['input']}, output: {output}, expected: {question['output']}")
    