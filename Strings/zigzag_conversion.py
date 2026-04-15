def zigzag_conversion(s, numRows):
    if numRows == 1:
        return s
    rows = [""] * numRows
    curr_row = 0
    direction = 1
    for char in s:
        rows[curr_row] += char
        if curr_row == 0:
            direction = 1
        elif curr_row == numRows-1:
            direction = -1
        curr_row += direction
    return "".join(rows)

s = "GOOGLEISHIRING"
numRows = 3
print(zigzag_conversion(s, numRows))