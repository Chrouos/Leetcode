from typing import List, Optional
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
    
    def tree_print_list(self, root):
        if not root: return []
        
        queue = [root]
        result = []
        while queue:
            node = queue.pop(0)
            if node is None:
                result.append(None)
                continue
            
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        
        # 去除末尾的 None
        while result and result[-1] is None:
            result.pop()
        
        return result
    
    
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        '''
        交換左右樹
        '''
        
        if not root: return None
        
        # 交換左右子樹
        root.left, root.right = root.right, root.left

        # 遞迴處理子樹
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


if __name__ == "__main__":
    
    s = Solution()
    question_list = [
        {"input": [[4,2,7,1,3,6,9]], "output": [4,7,2,9,6,3,1]},
        # {"input": [[1,2,3]], "output": [1,3,2]},
        # {"input": [[1]], "output": [1]},
        # {"input": [], "output": []}
    ]
    
    for question in question_list:
        p = TreeNode().list_to_tree(question['input'][0])

        output = p.tree_print_list(s.invertTree(p))
        print(f"[{output == question['output']}] input: {question['input']}, output: {output}, expected: {question['output']}")
        