# #brute force
# from collections import deque
# def max_area_island(grid):
#     rows, cols = len(grid), len(grid[0])
#     visited = [[False] * cols for _ in range(rows)]
#     max_area = 0
#
#     for r in range(rows):
#         for c in range(cols):
#             if grid[r][c] == 1 and not visited[r][c]:
#                 area = 0
#                 q = deque([(r, c)])
#                 visited[r][c] = True
#
#                 while q:
#                     row, col = q.popleft()
#                     area += 1
#
#                     for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#                         nr, nc = row + dr, col + dc
#                         if 0 <= nr < rows and 0 <= nc < cols:
#                             if grid[nr][nc] == 1 and not visited[nr][nc]:
#                                 visited[nr][nc] = True
#                                 q.append((nr, nc))
#
#                 max_area = max(max_area, area)
#
#     return max_area



#optimized
def max_area_island(grid):
    rows, cols = len(grid), len(grid[0])
    max_area = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                area = 0
                q = deque([(r, c)])
                grid[r][c] = 0

                while q:
                    row, col = q.popleft()
                    area += 1

                    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nr, nc = row + dr, col + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            grid[nr][nc] = 0
                            q.append((nr, nc))

                max_area = max(max_area, area)

    return max_area
