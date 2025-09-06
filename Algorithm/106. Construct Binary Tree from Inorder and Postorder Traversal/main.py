from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def list_to_tree(self, lst):
        # （小修）空列表直接回傳 None
        if not lst:
            return None
        
        root = TreeNode(lst[0])
        queue = [root]
        index = 1
        while queue:
            node = queue.pop(0)
            if node is None:
                continue
            if index >= len(lst):
                break
            
            node.left = TreeNode(lst[index]) if lst[index] is not None else None
            queue.append(node.left)
            index += 1
            
            if index >= len(lst):
                break
            node.right = TreeNode(lst[index]) if lst[index] is not None else None
            queue.append(node.right)
            index += 1
                
        return root
    
    def tree_print_list(self, root):
        if not root:
            return []
        
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        '''
        由中序(inorder)與後序(postorder)重建二元樹。
        觀念：postorder 最後一個是根；用 inorder 把左右子樹切段。
        注意：因為 postorder 是 左→右→根，從尾端往前取時要先建「右子樹」再建「左子樹」。
        '''
        
        if not inorder or not postorder or len(inorder) != len(postorder):
            return None
        
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        post_idx = len(postorder) - 1
        
        def helper(left: int, right: int) -> Optional[TreeNode]:
            nonlocal post_idx
            if left > right: return None
            
            root_val = postorder[post_idx]
            post_idx -= 1
            root = TreeNode(root_val)
            
            inorder_idx = idx_map[root_val]
            # 注意：先建右子樹再建左子樹
            root.right = helper(inorder_idx + 1, right)
            root.left = helper(left, inorder_idx - 1)
            return root

        return helper(0, len(inorder) - 1)
    
if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": ([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]), "output": [3, 9, 20, None, None, 15, 7]},
        {"input": ([1], [1]), "output": [1]},
    ]
    
    for q in question_list:
        inorder, postorder = q["input"]
        root = s.buildTree(inorder, postorder)
        output = TreeNode().tree_print_list(root)
        print(f"[{output == q['output']}] input: {q['input']}, output: {output}, expected: {q['output']}")
