#brute force
# def flood_fill(image, sr, sc, color):
    # rows, cols = len(image), len(image[0])
    # original = image[sr][sc]
    #
    # if original == color:
    #     return image
    #
    # q = deque()
    # q.append((sr, sc))
    # image[sr][sc] = color
    #
    # while q:
    #     r, c = q.popleft()
    #
    #     for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
    #         nr, nc = r + dr, c + dc
    #         if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == original:
    #             image[nr][nc] = color
    #             q.append((nr, nc))
    #
    # return image

#optmized
def flood_fill(image, sr, sc, color):
    rows, cols = len(image), len(image[0])
    original = image[sr][sc]

    if original == color:
        return image

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if image[r][c] != original:
            return

        image[r][c] = color

        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    dfs(sr, sc)
    return image