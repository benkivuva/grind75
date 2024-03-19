#!/usr/bin/env python3

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

# Test cases
if __name__ == "__main__":
    # Test case 1
    root1 = TreeNode(4)
    root1.left = TreeNode(2)
    root1.right = TreeNode(7)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(3)
    root1.right.left = TreeNode(6)
    root1.right.right = TreeNode(9)

    solution = Solution()
    inverted_tree1 = solution.invertTree(root1)

    print("Test case 1:", end=" ")
    # Function to print the tree in pre-order traversal
    def print_tree(node):
        if not node:
            return
        print(node.val, end=" ")
        print_tree(node.left)
        print_tree(node.right)
    print_tree(inverted_tree1)
    print()

    # Test case 2
    root2 = TreeNode(2)
    root2.left = TreeNode(1)
    root2.right = TreeNode(3)

    inverted_tree2 = solution.invertTree(root2)

    print("Test case 2:", end=" ")
    print_tree(inverted_tree2)
    print()

    # Test case 3
    root3 = None

    inverted_tree3 = solution.invertTree(root3)

    print("Test case 3:", end=" ")
    print_tree(inverted_tree3)
    print()