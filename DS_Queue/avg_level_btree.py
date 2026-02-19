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

#space Optimized
def avg(root):
    sums = []
    counts = []
    def dfs(node,level):
        if not node:
            return
        if level == len(sums):
            sums.append(0)
            counts.append(0)
        sums[level] += node.val
        counts[level] += 1
        dfs(node.left,level+1)
        dfs(node.right,level+1)
    dfs(root,0)
    return [sums[i]/counts[i] for i in range(len(sums))]