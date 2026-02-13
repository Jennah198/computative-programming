# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder, postorder):
        # Map value -> inorder index
        index_map = {val: i for i, val in enumerate(inorder)}

        self.post_idx = len(postorder) - 1

        def build(left, right):
            if left > right:
                return None

            # Root from postorder
            root_val = postorder[self.post_idx]
            self.post_idx -= 1

            root = TreeNode(root_val)

            # Split inorder
            mid = index_map[root_val]

            # Build RIGHT first
            root.right = build(mid + 1, right)
            root.left = build(left, mid - 1)

            return root

        return build(0, len(inorder) - 1)
