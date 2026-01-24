class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder_traversal(root):
    result = []

    def dfs(node):
        if not node:
            return
        result.append(node.val)  # ROOT
        dfs(node.left)           # LEFT
        dfs(node.right)          # RIGHT

    dfs(root)
    return result

# Build the tree
root = TreeNode(1)
root.left =TreeNode(4)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
root.right.right = TreeNode(7)

print(preorder_traversal(root))