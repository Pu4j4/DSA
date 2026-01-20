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

