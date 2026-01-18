from collections import deque

def avg_level(root):
    if not root:
        return []
    result = []
    q = deque([root])
    while q:
        level_size = len(q)
        level_sum = 0
        for _ in range(level_size):
            node = q.popleft()
            level_sum += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(level_sum/level_size)
    return result