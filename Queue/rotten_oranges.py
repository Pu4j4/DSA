def oranges_rotting(grid):
    rows, cols = len(grid), len(grid[0])
    minutes = 0

    while True:
        to_rot = []

        # Step 1: scan entire grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            to_rot.append((nr, nc))

        # Step 2: if nothing can rot
        if not to_rot:
            break

        # Step 3: rot all collected oranges
        for r, c in to_rot:
            grid[r][c] = 2

        minutes += 1

    # Step 4: check if fresh oranges remain
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                return -1

    return minutes
